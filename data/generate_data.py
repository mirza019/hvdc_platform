# data/generate_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_hvdc_data(num_entries=10000):
    """Generates synthetic HVDC data with voltage, current, and power."""
    # Start time and generate timestamps for each minute
    start_time = datetime.now()
    timestamps = [start_time + timedelta(minutes=i) for i in range(num_entries)]
    
    # Generate synthetic data for voltage and current
    voltage = np.random.normal(500, 10, num_entries)  # Voltage in kV
    current = np.random.normal(1.5, 0.1, num_entries)  # Current in kA
    
    # Calculate power based on voltage and current
    power = voltage * current

    # Create a DataFrame to hold the data
    data = pd.DataFrame({
        "Time": timestamps,
        "Voltage": voltage,
        "Current": current,
        "Power": power
    })

    # Save the generated data to CSV
    data.to_csv("data/hvdc_data.csv", index=False)
    print("Generated 10,000 data points and saved to data/hvdc_data.csv")

# Generate the data
generate_hvdc_data()
