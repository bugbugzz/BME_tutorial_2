# Plotting live data

import csv
import time
from CreaTeBME import SensorManager
import pandas as pd
import matplotlib.pyplot as plt


# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['6412'])
var_names = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z'] #


# Start the sensor manager
manager.start()

acc_x = []

while True:
    measurements = manager.get_measurements()
    for sensor, data in measurements.items():
        if not data: continue
        print(sensor, data)
        print(data[0][0])
        acc_x.append(data[0][0])

        plt.clf()
        plt.plot(acc_x, label='acc_x')
        plt.pause(0.05)

# Stop the sensor manager
manager.stop()
file.close()
