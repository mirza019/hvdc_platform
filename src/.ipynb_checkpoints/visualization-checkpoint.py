# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_voltage_current(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Time'], data['Voltage'], label='Voltage (kV)', color='blue')
    plt.plot(data['Time'], data['Current'], label='Current (kA)', color='orange')
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.legend()
    plt.title("Voltage and Current Trends Over Time")
    plt.savefig("figures/voltage_current_trend.png")
    plt.close()

def plot_distribution(data):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(data['Voltage'], kde=True, color='blue')
    plt.title("Voltage Distribution")
    plt.xlabel("Voltage (kV)")

    plt.subplot(1, 2, 2)
    sns.histplot(data['Current'], kde=True, color='orange')
    plt.title("Current Distribution")
    plt.xlabel("Current (kA)")
    plt.tight_layout()
    plt.savefig("figures/distribution.png")
    plt.close()

def plot_voltage_current_relationship(data):
    plt.figure(figsize=(8, 5))
    plt.scatter(data['Voltage'], data['Current'], alpha=0.5, color='green')
    plt.xlabel("Voltage (kV)")
    plt.ylabel("Current (kA)")
    plt.title("Voltage vs. Current Relationship")
    plt.savefig("figures/voltage_current_relationship.png")
    plt.close()

def plot_correlation_heatmap(data):
    plt.figure(figsize=(6, 5))
    corr_matrix = data[['Voltage', 'Current', 'Power']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Heatmap")
    plt.savefig("figures/correlation_heatmap.png")
    plt.close()

def plot_optimization_progress(progress):
    if not progress:
        print("No data to plot for optimization progress.")
        return
    
    plt.figure(figsize=(8, 5))
    plt.plot(progress, marker='o', color='purple')
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("Optimization Progress")
    plt.savefig("figures/optimization_progress.png")
    plt.close()
