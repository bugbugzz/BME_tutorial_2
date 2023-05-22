# Writes sensor data to a CSV

import csv
import time
from CreaTeBME import SensorManager

# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['6412'])

file = open('sensor_data/data1.csv', 'w')
writer = csv.writer(file)



# Start the sensor manager
manager.start()

while True:
    measurements = manager.get_measurements()
    for sensor, data in measurements.items():
        if not data: continue
        print(sensor, data)
        writer.writerow(data[0])


# Stop the sensor manager
manager.stop()
file.close()
