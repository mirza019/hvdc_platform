# simulation.py
import pandas as pd
import numpy as np
from time import sleep
from kafka import KafkaProducer

def generate_hvdc_data():
    # Create a continuous stream of data
    voltage = np.random.normal(500, 10)  # Voltage in kV
    current = np.random.normal(1.5, 0.1)  # Current in kA
    power = voltage * current  # Power in MW
    return {"voltage": voltage, "current": current, "power": power}

# Kafka setup (or replace with a simpler solution if needed)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

while True:
    data = generate_hvdc_data()
    producer.send('hvdc_data', value=str(data).encode())
    sleep(1)  # Send data every second
