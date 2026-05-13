/* ---- Sampling Time ---- */
#define DT 0.005f            // 200Hz -> 1/200 = 0.005s
// THIS TELLS THE MATH THAT EVERYTIME THE LOOP HAS RUNNED, 0.005s HAS PASSED

/* ---- PID Gains (SET TO ZERO FOR NOW TO FIND SETPOINT) ---- */
#define KP  40.0f
#define KI  0.1f
#define KD  1.5f

/* ---- Setpoint ---- */
// Target angle. You will change this number after reading the serial monitor!
#define SETPOINT 0.0f

/* ---- Output Limits ---- */
#define PID_OUT_MAX  999.0f   // TIM3 period = 999, max PWM, cap at 99%
#define PID_OUT_MIN -999.0f   

/* ---- Integral Anti-Windup Limit ---- */
#define INTEGRAL_MAX  200.0f
#define INTEGRAL_MIN -200.0f

/* ---- Complementary Filter Weights ---- */
#define COMP_GYRO_WEIGHT  0.98f
#define COMP_ACC_WEIGHT   0.02f

/* USER CODE BEGIN PV */
/* ---- Angle Estimation Variables ---- */
volatile float shared_angle   = 0.0f;   // Bridge between ISR and main
volatile float shared_pid_out = 0.0f;   // PID output for display
volatile uint8_t display_flag = 0;
static float filtered_derivative = 0.0f;
// For display/debug in main loop
float gyro_rate = 0.0f;
float acc_angle = 0.0f;
/* USER CODE END PV */

/* ============================================================
 * I3G4250D (Gyroscope) SPI Read/Write
 * ============================================================ */
void I3G_WriteReg(uint8_t reg_addr, uint8_t data) {
    uint8_t tx_buffer[2];
    tx_buffer[0] = reg_addr & 0x7F;  // Bit 7 = 0 for WRITE
    tx_buffer[1] = data;

    // FIX 2: Changed HAL_MAX_DELAY to 5ms timeout to prevent ISR hang
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_RESET); // CS LOW
    HAL_SPI_Transmit(&hspi1, tx_buffer, 2, 5);
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_SET);   // CS HIGH
}

uint8_t I3G_ReadReg(uint8_t reg_addr) {
    uint8_t tx_data = reg_addr | 0x80;  // Bit 7 = 1 for READ
    uint8_t rx_data = 0;

    // FIX 2: Changed HAL_MAX_DELAY to 5ms timeout to prevent ISR hang
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_RESET);
    HAL_SPI_Transmit(&hspi1, &tx_data, 1, 5);
    HAL_SPI_Receive(&hspi1, &rx_data, 1, 5);
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_3, GPIO_PIN_SET);

    return rx_data;
}

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim) {

    if (htim->Instance == TIM2) {

        static float tilt_angle    = 0.0f;
        static float integral      = 0.0f;
        static float prev_error    = 0.0f;
        static int   uart_counter  = 0;

        // --- CALIBRATION VARIABLES ---
        static int   calib_counter    = 0;
        static float gyro_y_sum       = 0.0f;
        static float acc_angle_sum    = 0.0f;
        static float gyro_y_offset    = 0.0f;
        static float acc_angle_offset = 0.0f;

        /* --- STEP 1: GYRO --- */
        uint8_t y_low  = I3G_ReadReg(0x2A);  // OUT_Y_L
        uint8_t y_high = I3G_ReadReg(0x2B);  // OUT_Y_H

        //Sensors store data in 8-bit chunks. We shift the 
        //"High" byte by 8 bits and OR it with the "Low" byte to 
        // get a full 16-bit signed integer.

        int16_t raw_gyro_y = (int16_t)((y_high << 8) | y_low);
        float gyro_y_dps = (float)raw_gyro_y * 0.00875f; // sensitivity

        /* --- STEP 2: ACCEL --- */
        // FIX 1: Reduced I2C timeout from 10 to 2ms to prevent ISR overrun
        uint8_t acc_reg = 0x28 | 0x80;
        uint8_t acc_buf[6] = {0};
        HAL_I2C_Master_Transmit(&hi2c1, 0x32, &acc_reg, 1, 2);
        HAL_I2C_Master_Receive(&hi2c1, 0x33, acc_buf, 6, 2);
        int16_t acc_raw_x = (int16_t)((acc_buf[1] << 8) | acc_buf[0]);
        int16_t acc_raw_z = (int16_t)((acc_buf[5] << 8) | acc_buf[4]);
        float acc_angle_deg = atan2f((float)acc_raw_x, (float)acc_raw_z) * (180.0f / 3.14159f);

        /* ====================================================
         * CALIBRATION ROUTINE (First 250 Samples = 1.25s)
           It just calculates the average "error" (offset) of the 
           sensors while the robot is still.
         * ==================================================== */
        if (calib_counter < 250) {
            // Accumulate readings
            gyro_y_sum    += gyro_y_dps;
            acc_angle_sum += acc_angle_deg;
            calib_counter++;

            // Ensure motors remain stopped during calibration
            Motor_Left_Stop();
            Motor_Right_Stop();

            return; // Skip the rest of the ISR (Comp Filter, PID, Drive)
        }
        else if (calib_counter == 250) {
            // Calculate average offsets
            gyro_y_offset    = gyro_y_sum / 250.0f;
            acc_angle_offset = acc_angle_sum / 250.0f;

            // Set starting tilt to exactly 0 to prevent initial jumps
            tilt_angle = 0.0f;  // angle after calibration set to zero

            calib_counter++; // Move to state 251 (Normal Operation)
            return;
        }

        /* ====================================================
         * NORMAL OPERATION
         * ==================================================== */
        // Apply calculated offsets to zero-out the sensors
        gyro_y_dps    -= gyro_y_offset;
        acc_angle_deg -= acc_angle_offset;

        /* --- STEP 3: COMP FILTER --- 
        Part 1: (tilt_angle + gyro_y_dps * DT) is Integration. 
        If you are rotating at 10 degree/sec for 0.005s, you have moved 
        0.05 degrees. We add that to the previous angle.
        Part 2: We multiply the Gyro result by 0.98 and the Accelerometer result by 0.02. 
        This "trusts" the smooth gyro for short-term changes but uses the 
        steady accelerometer to prevent the gyro from "drifting" over time.*/
        tilt_angle = COMP_GYRO_WEIGHT * (tilt_angle + gyro_y_dps * DT)
                   + COMP_ACC_WEIGHT  * acc_angle_deg; 

        /* --- STEP 4: PID --- 
        P-Term: KP * error. If the error is big, the push is big.

        I-Term: integral += KI * error * DT. This adds up the error over time. 
        If the robot has been leaning for a while, the integral grows to force it back.

        D-Term: (error - prev_error) / DT. This is the Slope. 
        If the error is changing very fast (the robot is falling quickly), 
        the D-term provides a counter-force to "brake" the fall.*/
        float error = SETPOINT - tilt_angle;

        float p_term = KP * error;

        integral += KI * error * DT;
        if (integral > INTEGRAL_MAX) integral = INTEGRAL_MAX;
        if (integral < INTEGRAL_MIN) integral = INTEGRAL_MIN;

        float raw_derivative = (error - prev_error) / DT;

        /*Filtering D: 0.7f * filtered_derivative + 0.3f * raw_derivative. 
        This is a digital low-pass filter. It prevents high-frequency 
        electrical noise from making motors jitter.*/

        filtered_derivative = 0.7f * filtered_derivative + 0.3f * raw_derivative;
        float d_term = KD * filtered_derivative;
        prev_error = error;
        
        // PID FORMULA
        float pid_output = p_term + integral + d_term;

        if (pid_output > PID_OUT_MAX) pid_output = PID_OUT_MAX;
        if (pid_output < PID_OUT_MIN) pid_output = PID_OUT_MIN;

        /* --- STEP 5: DRIVE --- */
        Motors_Drive(pid_output);

        /* --- STEP 6: SHARED VARS --- */
        shared_angle   = tilt_angle;
        shared_pid_out = pid_output;
        gyro_rate      = gyro_y_dps;
        acc_angle      = acc_angle_deg;

        /* --- STEP 7: UART THROTTLE (10Hz) --- */
        if (++uart_counter >= 20) {
            display_flag = 1;
            uart_counter = 0;
        }
    }
}

/*void Motor_Left_Forward(uint16_t speed) {
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_7, GPIO_PIN_SET);    // PE7 = HIGH
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_6, GPIO_PIN_RESET);  // PE6 = LOW
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_2, speed);
}

void Motor_Left_Backward(uint16_t speed) {
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_7, GPIO_PIN_RESET);  // PE7 = LOW
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_6, GPIO_PIN_SET);    // PE6 = HIGH
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_2, speed); //If speed is 500, 
    //the pin stays HIGH for 500 clock ticks and LOW for 499 ticks (50% duty cycle).
}

void Motor_Left_Stop(void) {
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_7, GPIO_PIN_SET);
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_6, GPIO_PIN_SET);
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_2, 0);
}

void Motor_Right_Forward(uint16_t speed) {
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_8, GPIO_PIN_SET);    // PE8 = HIGH
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_12, GPIO_PIN_RESET); // PE12 = LOW
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, speed);
}

void Motor_Right_Backward(uint16_t speed) {
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_8, GPIO_PIN_RESET);  // PE8 = LOW
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_12, GPIO_PIN_SET);   // PE12 = HIGH
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, speed);
}

void Motor_Right_Stop(void) {
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_8, GPIO_PIN_SET);
    HAL_GPIO_WritePin(GPIOE, GPIO_PIN_12, GPIO_PIN_SET);
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, 0);
}*/

void Motors_Drive(float pid_output) {
    uint16_t pwm_val;

    if (pid_output > 0) {
        if (pid_output > PID_OUT_MAX) pid_output = PID_OUT_MAX;
        pwm_val = (uint16_t)pid_output;
        Motor_Left_Forward(pwm_val);
        Motor_Right_Forward(pwm_val);
    }
    else if (pid_output < 0) {
        float abs_out = -pid_output;
        if (abs_out > PID_OUT_MAX) abs_out = PID_OUT_MAX;
        pwm_val = (uint16_t)abs_out;
        Motor_Left_Backward(pwm_val);
        Motor_Right_Backward(pwm_val);
    }
    else {
        Motor_Left_Stop();
        Motor_Right_Stop();
    }
}

/* ============================================================
 * UART Print Helper - Optimized for Bluetooth
 * HAL_MAX_DELAY to 100ms timeout
 * Use %.2f directly — fixes negative angle display bug
 * ============================================================ */
void cout(const char *fmt, ...) {
    char buffer[128];
    va_list args;
    va_start(args, fmt);
    int l = vsnprintf(buffer, sizeof(buffer), fmt, args);
    va_end(args);
    if (l > 0) {
        HAL_UART_Transmit(&huart2, (uint8_t*)buffer, l, 100); 
    }
}

int main(void)
{

  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_I2C1_Init();
  MX_SPI1_Init();
  MX_TIM3_Init();
  MX_USB_PCD_Init();
  MX_I2C2_Init();
  MX_TIM2_Init();
  MX_USART2_UART_Init();

  /* USER CODE BEGIN 2 */
  HAL_Delay(500); // Give UART/Bluetooth time to wake up
  cout("Bluetooth System Starting...\r\n");
  /* USER CODE END 2 */

  // ---- Initialize Gyroscope (I3G4250D via SPI) ----
  // CTRL_REG1 = 0x20: 200Hz ODR, normal mode, XYZ enable
  I3G_WriteReg(0x20, 0x4F);

  // ---- Initialize Accelerometer (LSM303DLHC via I2C) ----
  // CTRL_REG1_A = 0x20, value 0x57 = 100Hz, normal mode, XYZ enabled
  uint8_t acc_init[2] = {0x20, 0x57};
  HAL_I2C_Master_Transmit(&hi2c1, 0x32, acc_init, 2, 50);

  // ---- Start PWM on both channels for motor speed control ----
  HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_1);
  HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_2);

  // Initialize motors stopped
  Motor_Left_Stop();
  Motor_Right_Stop();

  // ---- Start TIM2 interrupt for 200Hz control loop ----
  HAL_TIM_Base_Start_IT(&htim2);

  // Small delay to let sensors settle
  HAL_Delay(100);

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  /* Infinite loop */
  while (1)
  {
      /* UPDATE YOUR PRINT FORMAT TO MATCH THE APP'S "E" REQUIREMENT */
if (display_flag == 1) {
    display_flag = 0;

    // Convert floats to integers as we did before
    int ang_i = (int)shared_angle;
    int ang_f = (int)(fabsf(shared_angle - (float)ang_i) * 100.0f);
    int gyr_i = (int)gyro_rate;
    int gyr_f = (int)(fabsf(gyro_rate - (float)gyr_i) * 100.0f);
    int acc_i = (int)acc_angle;
    int acc_f = (int)(fabsf(acc_angle - (float)acc_i) * 100.0f);

    /* * THE APP REQUIREMENT: Evalue1,value2,value3\n
     * Note: No spaces, just the 'E' then comamas.
     */
    cout("E%d.%02d,%d.%02d,%d.%02d\n", 
          ang_i, ang_f, 
          gyr_i, gyr_f, 
          acc_i, acc_f);
}
  }
  /* USER CODE END 3 */
}