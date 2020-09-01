#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, InfraredSensor, GyroSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize a motors at port A and D
right_motor = Motor(Port.A)
left_motor = Motor(Port.D)

# Initialize the Infrared sensor and Gyroscopic sensor (Gyrosensor) 
"""
Infrared sensor: 

Gyrosensor:

"""
#infrared_sensor = InfraredSensor(Port.S3) why aren't you working??
gyro_sensor = GyroSensor(Port.S2)

# Reset gyro [confirm this]

# Read gyro sensor data 
# Seems to be working if we access the speed and angles individually

for i in range(0,100):
    # Use panda data frame to write data to csv file to confirm if the angular velocity and robot angle
# are being outputted
    print("Angular velocity: {}\n".format(gyro_sensor.speed()))

print("-*-*-*-*-*-*-*-*-*-*-*-*")

for i in range(0,100):
    print("Robot angle: {}\n".format(gyro_sensor.angle()))
    

# Do the covariance or variance thing on "excel"


# Kalman Filter
# do we also use motor encoders for this?


# PID Controller

# Go back to motor initialization and confirm if we need more 
# options to be specified, ie, direction, gear train ratio etc

# Include a battery voltage check

# Add a sound file when robot falling over? This has a potential
# to become annoying quickly :D

# Display distance on display using infrared sensor. 

# Use sensor for obstacle avoidance

# Other infrared sensor challenges:
# Make your robot seek out and drive towards the infrared beacon.
# Use the infrared beacon as a remote control for your robot.

if __name__ == "__main__":
    pass
    # Define methods for different purposes
    # Main balancing function should be in a loop, how do we initialize?
    # Use try except block then output error
    
    
# Strive to get this project sent to ev3dev. No pressure, but something to strive for, keep pushing
