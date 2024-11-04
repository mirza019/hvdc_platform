# data_processing.py
import pandas as pd
from datetime import datetime

def preprocess_data(data):
    # Convert to DataFrame and handle outliers
    df = pd.DataFrame(data)
    df["Time"] = datetime.now()
    df = df[df["voltage"].between(480, 520)]
    return df

# Example usage with dummy data
data = [{"voltage": 510, "current": 1.6, "power": 816}]
processed_data = preprocess_data(data)
print(processed_data)
