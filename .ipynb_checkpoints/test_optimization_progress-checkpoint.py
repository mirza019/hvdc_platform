# test_optimization_progress.py
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

def complex_loss(x):
    """A more complex loss function with a minimum at (3, 2)."""
    # Adding a sinusoidal component to make the optimization path more complex
    return (x[0] - 3)**2 + (x[1] - 2)**2 + 0.1 * (x[0] * x[1]) * np.sin(x[0] * x[1])

def optimize_with_progress():
    """Optimize a complex function and track the loss at each iteration."""
    progress = []

    def callback(xk):
        """Callback to capture loss at each iteration."""
        loss = complex_loss(xk)
        print(f"Callback: Params = {xk}, Loss = {loss}")
        progress.append(loss)  # Store each loss value

    # Start optimization with a farther initial guess
    result = minimize(complex_loss, [-10, -10], bounds=[(-10, 10), (-10, 10)], callback=callback)
    optimal_x, optimal_y = result.x
    print("Optimization completed.")
    print("Optimal X:", optimal_x)
    print("Optimal Y:", optimal_y)
    print("Optimization Progress:", progress)
    return progress

def plot_progress(progress):
    """Plot optimization progress showing the loss per iteration."""
    if not progress:
        print("No progress data to plot.")
        return
    
    plt.figure(figsize=(8, 5))
    plt.plot(progress, marker='o', color='purple')
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("Optimization Progress")
    plt.show()

# Run the test
if __name__ == "__main__":
    progress = optimize_with_progress()
    plot_progress(progress)
