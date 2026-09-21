import math
import random
import matplotlib.pyplot as plt

# ==========================================
# 1. Benchmark Functions
# ==========================================

def booth(x, y):
    # Booth function: minimum is at (1, 3) where f = 0
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def himmelblau(x, y):
    # Himmelblau function: has 4 global minima where f = 0
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def griewank(x, y):
    # Griewank function: minimum is at (0, 0) where f = 0
    return 1 + (x**2 + y**2) / 4000 - math.cos(x) * math.cos(y / math.sqrt(2))


# ==========================================
# 2. Simulated Annealing Algorithm
# ==========================================

def run_simulated_annealing(func, bounds, T_start=50.0, decay=1, K=100, step=0.5):
    # Get the domain min and max limits
    low_bound, high_bound = bounds
    
    # Pick a random starting point inside the domain
    current_x = random.uniform(low_bound, high_bound)
    current_y = random.uniform(low_bound, high_bound)
    current_val = func(current_x, current_y)
    
    # Keep track of the best solution found so far
    best_x = current_x
    best_y = current_y
    best_val = current_val
    
    # Lists to store history for plotting graphs
    x_history = [current_x]
    y_history = [current_y]
    f_history = [current_val]
    
    temp = T_start
    
    # Run until temperature drops to near zero
    while temp > 0.001:
        # Perform K iterations at the current temperature stage
        for i in range(K):
            # Pick a new point nearby within the neighborhood step size
            next_x = current_x + random.uniform(-step, step)
            next_y = current_y + random.uniform(-step, step)
            
            # Make sure the new point stays within domain boundaries
            next_x = max(low_bound, min(high_bound, next_x))
            next_y = max(low_bound, min(high_bound, next_y))
            
            # Calculate the value at the new point
            next_val = func(next_x, next_y)
            delta = next_val - current_val
            
            # Decision:
            # If the new point is better (lower function value), always take it.
            if delta < 0:
                current_x = next_x
                current_y = next_y
                current_val = next_val
            else:
                # If it's worse, compare it with a 'r', accept if less than the acceptance probability
                acceptance_prob = math.exp(-delta / temp)
                if random.random() < acceptance_prob:
                    current_x = next_x
                    current_y = next_y
                    current_val = next_val
            
            # Update best found solution
            if current_val < best_val:
                best_x = current_x
                best_y = current_y
                best_val = current_val
            
            # Store values for plotting later
            x_history.append(current_x)
            y_history.append(current_y)
            f_history.append(current_val)
        
        # Cool down the temperature by decay step after every K iterations
        temp = temp*0.95
        
    return (best_x, best_y, best_val), (x_history, y_history, f_history)


# ==========================================
# 3. Plotting Graph Helper Function
# ==========================================

def plot_results(title, x_hist, y_hist, f_hist):
    iterations = range(len(f_hist))
    
    plt.figure(figsize=(8, 6))
    
    # Top plot: Function value f(x, y) over iterations
    plt.subplot(2, 1, 1)
    plt.plot(iterations, f_hist, 'r.-', label='Objective Value', markersize=3)
    plt.title(f"Simulated Annealing - {title}")
    plt.ylabel('f(x, y)')
    plt.grid(True)
    plt.legend()
    
    # Bottom plot: x and y values over iterations
    plt.subplot(2, 1, 2)
    plt.plot(iterations, x_hist, 'b.-', label='x', markersize=3)
    plt.plot(iterations, y_hist, 'g.--', label='y', markersize=3)
    plt.xlabel('Iteration')
    plt.ylabel('Variables')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()


# ==========================================
# 4. Running the Code
# ==========================================

if __name__ == "__main__":
    # Test Booth Function [-10, 10]
    print("Testing Booth Function...")
    best, history = run_simulated_annealing(booth, (-10.0, 10.0))
    print(f"Best Point: x = {best[0]:.4f}, y = {best[1]:.4f}")
    print(f"Minimum Value: {best[2]:.4f}\n")
    plot_results("Booth Function", history[0], history[1], history[2])

    # Test Himmelblau Function [-5, 5]
    print("Testing Himmelblau Function...")
    best, history = run_simulated_annealing(himmelblau, (-5.0, 5.0))
    print(f"Best Point: x = {best[0]:.4f}, y = {best[1]:.4f}")
    print(f"Minimum Value: {best[2]:.4f}\n")
    plot_results("Himmelblau Function", history[0], history[1], history[2])

    # Test Griewank Function [-30, 30]
    print("Testing Griewank Function...")
    best, history = run_simulated_annealing(griewank, (-30.0, 30.0))
    print(f"Best Point: x = {best[0]:.4f}, y = {best[1]:.4f}")
    print(f"Minimum Value: {best[2]:.4f}\n")
    plot_results("Griewank Function", history[0], history[1], history[2])