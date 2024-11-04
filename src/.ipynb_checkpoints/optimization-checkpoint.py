# src/optimization.py
import numpy as np
from scipy.optimize import minimize

def complex_efficiency_loss(params):
    """A more complex efficiency loss function with sinusoidal component."""
    voltage, current = params
    power_loss = voltage * current * 0.1
    efficiency = voltage * current / power_loss
    # Adding a sinusoidal component to make the loss function more complex
    return -efficiency + 0.1 * np.sin(voltage * current)

def optimize_parameters():
    """Optimize voltage and current to maximize efficiency with progress tracking."""
    progress = []  # Track efficiency loss at each iteration

    def callback(xk):
        """Store efficiency loss for each iteration."""
        loss = complex_efficiency_loss(xk)
        print(f"Callback: Params = {xk}, Loss = {loss}")
        progress.append(loss)  # Store each loss value

    # Use a farther initial guess to make the optimization take more steps
    result = minimize(complex_efficiency_loss, [480, 1.0], bounds=[(400, 600), (0.5, 2.5)], callback=callback)
    optimal_voltage, optimal_current = result.x  # Extract the optimal parameters
    
    # Print optimization results and progress
    print("Optimization completed.")
    print("Optimal Voltage:", optimal_voltage)
    print("Optimal Current:", optimal_current)
    print("Optimization Progress:", progress)
    return optimal_voltage, optimal_current, progress  # Return all three values
