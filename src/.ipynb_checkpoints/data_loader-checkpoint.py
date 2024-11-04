# src/data_loader.py
import pandas as pd
import config

def load_data():
    """Loads HVDC data from CSV and handles missing values."""
    data = pd.read_csv(config.DATA_PATH)
    data = data.ffill()  # Forward fill missing values
    return data
