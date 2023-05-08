# Plots the data (length) of multiple sensors to the serial monitor

import time
from CreaTeBME import SensorManager

# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['6412', '0FD6'])

# Start the sensor manager
manager.start()
print("Connected to SENSORS")

while True:
    measurements = manager.get_measurements()
    for sensor, data in measurements.items():
        if not data: continue
        print(sensor, len(data))

# Stop the sensor manager
manager.stop()
