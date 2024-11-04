# src/analysis.py

def calculate_averages(data):
    """Calculates average voltage and current."""
    avg_voltage = data['Voltage'].mean()
    avg_current = data['Current'].mean()
    return avg_voltage, avg_current

def detect_anomalies(data):
    """Detects anomalies in voltage and current."""
    voltage_anomalies = data[(data['Voltage'] < 480) | (data['Voltage'] > 520)]
    current_anomalies = data[(data['Current'] < 1.0) | (data['Current'] > 2.0)]
    return voltage_anomalies, current_anomalies
