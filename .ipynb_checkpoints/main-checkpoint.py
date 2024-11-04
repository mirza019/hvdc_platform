# main.py
from src.data_loader import load_data
from src.analysis import calculate_averages, detect_anomalies
from src.optimization import optimize_parameters
from src.visualization import (
    plot_voltage_current,
    plot_distribution,
    plot_voltage_current_relationship,
    plot_correlation_heatmap,
    plot_optimization_progress
)
import config

def main():
    # Step 1: Load data
    data = load_data()

    # Step 2: Data Analysis
    avg_voltage, avg_current = calculate_averages(data)
    voltage_anomalies, current_anomalies = detect_anomalies(data)

    # Step 3: Optimization
    optimal_voltage, optimal_current, optimization_progress = optimize_parameters()

    # Step 4: Visualization
    plot_voltage_current(data)
    plot_distribution(data)
    plot_voltage_current_relationship(data)
    plot_correlation_heatmap(data)
    plot_optimization_progress(optimization_progress)  # Show optimization convergence

    # Step 5: Generate Report
    with open(config.REPORT_PATH, 'w') as file:
        file.write("HVDC System Analysis Report\n")
        file.write("===========================\n\n")
        file.write(f"Average Voltage: {avg_voltage:.2f} kV\n")
        file.write(f"Average Current: {avg_current:.2f} kA\n\n")
        file.write("Detected Anomalies:\n")
        file.write(f"Voltage anomalies: {len(voltage_anomalies)}\n")
        file.write(f"Current anomalies: {len(current_anomalies)}\n\n")
        file.write("Optimal Parameters:\n")
        file.write(f"Optimal Voltage: {optimal_voltage:.2f} kV\n")
        file.write(f"Optimal Current: {optimal_current:.2f} kA\n")

    print("Report generated at:", config.REPORT_PATH)

if __name__ == "__main__":
    main()
