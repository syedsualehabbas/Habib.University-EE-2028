import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Physics parameters (matching the report)
B = 0.8  # Magnetic field strength (Tesla)
l = 0.5  # Length of rod (meters)
R = 5.0  # Resistance (Ohms)
m = 0.2  # Mass of rod (kg)
v0 = 2.0  # Initial velocity (m/s) - slower for better visualization

# External force options
F_ext = 0.0  # External force (Newtons)
apply_force = False

# Time tracking
t = 0.0
dt = 1.0 / FPS

# Rod state
v = v0  # Current velocity
x = 0.0  # Position

# Display scaling
pixels_per_meter = 150  # Increased for better visibility

# Create display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Electromagnetic Induction - Line Integrals & EMF")
clock = pygame.time.Clock()

# Fonts
font_small = pygame.font.Font(None, 24)
font = pygame.font.Font(None, 28)
title_font = pygame.font.Font(None, 40)

# Rail positions
rail_top_y = 250
rail_bottom_y = rail_top_y + int(l * pixels_per_meter)
rail_left_x = 150
rail_right_x = 1000

# Button class for UI
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover = False
    
    def draw(self, screen):
        color = tuple(min(c + 30, 255) for c in self.color) if self.hover else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        text_surf = font_small.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Create buttons
reset_button = Button(50, HEIGHT - 80, 120, 40, "Reset", BLUE)
force_button = Button(190, HEIGHT - 80, 180, 40, "Toggle Force", GREEN)

def calculate_tau():
    """Calculate time constant τ = mR / (B²l²)"""
    return (m * R) / (B**2 * l**2)

def calculate_terminal_velocity():
    """Calculate terminal velocity v_term = F₀R / (B²l²)"""
    if F_ext > 0:
        return (F_ext * R) / (B**2 * l**2)
    return 0

def update_physics(dt):
    """Update velocity and position based on differential equation"""
    global v, x, t
    
    # Calculate magnetic force: F_mag = -(B²l²/R)v
    F_mag = -(B**2 * l**2 / R) * v
    
    # Total force
    F_total = F_ext + F_mag
    
    # Acceleration: a = F/m
    a = F_total / m
    
    # Update velocity: dv/dt = a
    v += a * dt
    
    # Ensure velocity doesn't go negative
    if v < 0:
        v = 0
    
    # Update position
    x += v * dt
    
    # Update time
    t += dt

def calculate_emf():
    """Calculate induced EMF: ε = Blv"""
    return B * l * v

def calculate_current():
    """Calculate current: I = ε/R = Blv/R"""
    emf = calculate_emf()
    return emf / R if R > 0 else 0

def calculate_magnetic_flux():
    """Calculate magnetic flux: Φ = B·A = Blx"""
    return B * l * x

def calculate_power():
    """Calculate power dissipated: P = I²R"""
    I = calculate_current()
    return I**2 * R

def draw_circuit(rod_x_pixels):
    """Draw the circuit with rails, resistor, and moving rod"""
    # Draw rails
    pygame.draw.line(screen, GRAY, (rail_left_x, rail_top_y), (rail_right_x, rail_top_y), 5)
    pygame.draw.line(screen, GRAY, (rail_left_x, rail_bottom_y), (rail_right_x, rail_bottom_y), 5)
    
    # Draw resistor (zigzag)
    resistor_x = rail_left_x - 40
    resistor_points = []
    segments = 10
    segment_height = (rail_bottom_y - rail_top_y) / segments
    for i in range(segments + 1):
        y = rail_top_y + i * segment_height
        x = resistor_x + (18 if i % 2 == 0 else -18)
        resistor_points.append((x, y))
    pygame.draw.lines(screen, RED, False, resistor_points, 4)
    
    # Connect resistor to rails
    pygame.draw.line(screen, GRAY, (rail_left_x, rail_top_y), (resistor_x, rail_top_y), 5)
    pygame.draw.line(screen, GRAY, (rail_left_x, rail_bottom_y), (resistor_x, rail_bottom_y), 5)
    
    # Draw moving rod
    pygame.draw.line(screen, BLUE, (rod_x_pixels, rail_top_y), (rod_x_pixels, rail_bottom_y), 10)
    pygame.draw.circle(screen, CYAN, (rod_x_pixels, rail_top_y), 6)
    pygame.draw.circle(screen, CYAN, (rod_x_pixels, rail_bottom_y), 6)
    
    # Draw velocity arrow if moving
    if v > 0.01:
        arrow_len = min(70, v * 5)
        arrow_y = (rail_top_y + rail_bottom_y) // 2
        pygame.draw.line(screen, GREEN, (rod_x_pixels + 20, arrow_y), 
                        (rod_x_pixels + 20 + arrow_len, arrow_y), 5)
        # Arrowhead
        pygame.draw.polygon(screen, GREEN, [
            (rod_x_pixels + 20 + arrow_len, arrow_y),
            (rod_x_pixels + 20 + arrow_len - 12, arrow_y - 10),
            (rod_x_pixels + 20 + arrow_len - 12, arrow_y + 10)
        ])
    
    # Draw external force arrow if applied
    if apply_force and F_ext > 0:
        force_arrow_len = 60
        force_y = (rail_top_y + rail_bottom_y) // 2 + 40
        pygame.draw.line(screen, ORANGE, (rod_x_pixels - 30, force_y), 
                        (rod_x_pixels - 30 + force_arrow_len, force_y), 5)
        pygame.draw.polygon(screen, ORANGE, [
            (rod_x_pixels - 30 + force_arrow_len, force_y),
            (rod_x_pixels - 30 + force_arrow_len - 12, force_y - 10),
            (rod_x_pixels - 30 + force_arrow_len - 12, force_y + 10)
        ])
        f_text = font_small.render("F_ext", True, ORANGE)
        screen.blit(f_text, (rod_x_pixels - 20, force_y - 30))
    
    # Magnetic field indicators (X for into page)
    for x_pos in range(rail_left_x + 70, rail_right_x - 50, 100):
        for y_pos in range(rail_top_y + 50, rail_bottom_y - 20, 80):
            # Draw X
            size = 8
            pygame.draw.line(screen, YELLOW, (x_pos - size, y_pos - size), 
                           (x_pos + size, y_pos + size), 2)
            pygame.draw.line(screen, YELLOW, (x_pos - size, y_pos + size), 
                           (x_pos + size, y_pos - size), 2)
    
    # Label
    b_label = font.render("B (into page)", True, YELLOW)
    screen.blit(b_label, (rail_right_x - 180, rail_top_y - 35))

def draw_info():
    """Draw all information panels"""
    # Title
    title = title_font.render("EMF & Line Integrals - Moving Rod Simulation", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
    
    # Parameters panel
    param_y = 80
    param_title = font.render("Parameters:", True, CYAN)
    screen.blit(param_title, (50, param_y))
    
    params = [
        f"B = {B} T",
        f"l = {l} m",
        f"R = {R} Ω",
        f"m = {m} kg",
        f"F_ext = {F_ext} N" if apply_force else "F_ext = 0 N"
    ]
    
    for i, param in enumerate(params):
        text = font_small.render(param, True, WHITE)
        screen.blit(text, (50, param_y + 30 + i * 25))
    
    # Current state panel
    state_y = 80
    state_x = 300
    state_title = font.render("Current State:", True, CYAN)
    screen.blit(state_title, (state_x, state_y))
    
    emf = calculate_emf()
    I = calculate_current()
    flux = calculate_magnetic_flux()
    power = calculate_power()
    
    states = [
        f"Time: {t:.2f} s",
        f"Position: {x:.3f} m",
        f"Velocity: {v:.3f} m/s",
        f"EMF (ε): {emf:.4f} V",
        f"Current (I): {I:.4f} A"
    ]
    
    for i, state in enumerate(states):
        text = font_small.render(state, True, WHITE)
        screen.blit(text, (state_x, state_y + 30 + i * 25))
    
    # Calculations panel
    calc_y = 80
    calc_x = 600
    calc_title = font.render("Calculated Values:", True, CYAN)
    screen.blit(calc_title, (calc_x, calc_y))
    
    tau = calculate_tau()
    v_term = calculate_terminal_velocity()
    
    calcs = [
        f"Flux (Φ): {flux:.4f} Wb",
        f"Power (P): {power:.5f} W",
        f"F_mag: {-(B**2 * l**2 / R) * v:.4f} N",
        f"τ (tau): {tau:.3f} s",
        f"v_term: {v_term:.3f} m/s" if apply_force else ""
    ]
    
    for i, calc in enumerate(calcs):
        if calc:
            text = font_small.render(calc, True, WHITE)
            screen.blit(text, (calc_x, calc_y + 30 + i * 25))
    
    # Formulas
    formula_y = HEIGHT - 180
    formula_title = font.render("Key Formulas:", True, YELLOW)
    screen.blit(formula_title, (50, formula_y))
    
    formulas = [
        "ε = Blv",
        "I = ε/R = Blv/R",
        "F_mag = -IlB = -(B²l²/R)v",
        "m(dv/dt) = F_ext + F_mag",
        "Φ = Blx"
    ]
    
    for i, formula in enumerate(formulas):
        text = font_small.render(formula, True, GRAY)
        screen.blit(text, (50, formula_y + 30 + i * 22))
    
    # Case info
    case_y = formula_y
    case_x = 450
    if not apply_force:
        case_text = font.render("CASE I: No External Force", True, GREEN)
        screen.blit(case_text, (case_x, case_y))
        sol_text = font_small.render(f"Solution: v(t) = v₀·e^(-t/τ)", True, WHITE)
        screen.blit(sol_text, (case_x, case_y + 35))
        exp_text = font_small.render("Exponential decay to rest", True, GRAY)
        screen.blit(exp_text, (case_x, case_y + 60))
    else:
        case_text = font.render("CASE II: Constant Applied Force", True, ORANGE)
        screen.blit(case_text, (case_x, case_y))
        sol_text = font_small.render(f"Terminal velocity: v_term = {v_term:.3f} m/s", True, WHITE)
        screen.blit(sol_text, (case_x, case_y + 35))
        exp_text = font_small.render("Approaches steady state", True, GRAY)
        screen.blit(exp_text, (case_x, case_y + 60))

# Main loop
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_r:
                # Reset
                v = v0
                x = 0.0
                t = 0.0
        
        # Button events
        if reset_button.handle_event(event):
            v = v0
            x = 0.0
            t = 0.0
        
        if force_button.handle_event(event):
            apply_force = not apply_force
            F_ext = 0.5 if apply_force else 0.0  # Reduced force for slower movement
            # Reset when changing force mode
            v = v0
            x = 0.0
            t = 0.0
    
    # Update physics if not paused
    if not paused and v > 0.001:
        update_physics(dt)
    
    # Calculate rod position in pixels
    rod_x_pixels = rail_left_x + int(x * pixels_per_meter)
    
    # Reset if rod goes off screen
    if rod_x_pixels > rail_right_x - 50:
        x = 0.0
        t = 0.0
        if not apply_force:
            v = v0
    
    # Drawing
    screen.fill(BLACK)
    draw_circuit(rod_x_pixels)
    draw_info()
    
    # Draw buttons
    reset_button.draw(screen)
    force_button.draw(screen)
    
    # Instructions
    inst_text = font_small.render("SPACE: Pause/Resume  |  R: Reset  |  ESC: Quit", True, GRAY)
    screen.blit(inst_text, (WIDTH // 2 - inst_text.get_width() // 2, HEIGHT - 25))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()