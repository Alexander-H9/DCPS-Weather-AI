#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import math
from dbConnectionWindSpeed import *

# gpio pin 6
pin = 31    
time_interval = 10 		# intervall of sending data to influx in seconds   

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.IN)

db = InfluxDB()


# Anamometer vane diameter (set to the value for your cup-to-cup in mm)
vane_diameter = float(130)			# durchmesser von cup-mittelpunkt zu cup-mittelpunkt

# Calculate vane circumference in metres (umfang)
vane_circ = float (vane_diameter/1000)*math.pi

# Set an anamometer factor to account for inefficiency (value is a guess)
afactor = float(2.5)

# Start measuring wind speed
print('Measuring wind speed...')

# Define variables rotations and trigger (trigger = 1 if sensor triggered)
rotations = float(0)
trigger = 0

# Define variable endtime to be current time in seconds plus time_interval seconds
endtime = time.time() + time_interval	# 10

# Get initial state of sensor
sensorstart = GPIO.setup(pin,GPIO.IN)

while True:
	# measurement over time_interval seconds
	if endtime >= time.time():
		
		if GPIO.input(pin)==1 and trigger==0:
			rotations += 1
			trigger=1

		if GPIO.input(pin)==0:
			trigger = 0

	else:
		# 10 seconds has now finished. But if sensor triggered at start and did not move,
		# rotations value will be 1, which is wrong, so 
		if rotations==1 and sensorstart==1:
			rotations = 0

		# Calculate
		rots_per_second = float(rotations/time_interval)
		windspeed = float((rots_per_second)*vane_circ*afactor)

		print('{:.0f} rotations = {:.2f} rotations/second'.format(rotations, rotations/time_interval))
		print('Windspeed is {:.2f} m/s = '.format(windspeed))

		# setup the time for the next 10 seconds
		endtime = time.time() + time_interval

		# send data to database
		db.sendToInfluxDB("windSpeed", windspeed)


# # Measurement loop to run for 10 seconds
# while time.time() < endtime:
# 	if GPIO.input(pin)==1 and trigger==0:
# 		rotations += 1
# 		trigger=1
# 	if GPIO.input(pin)==0:
# 		trigger = 0
# 	# little delay to make things work reliably
# 	time.sleep(0.001)

# # Loop has now finished. But if sensor triggered at start and did not move,
# # rotations value will be 1, which is probably wrong, so 
# if rotations==1 and sensorstart==1:
# 	rotations = 0

# # Calculate
# rots_per_second = float(rotations/10)
# windspeed = float((rots_per_second)*vane_circ*afactor)

# # Print results with decent formatting
# print('{:.0f} rotations = {:.2f} rotations/second'.format(rotations, rotations/10))
# print('Windspeed is {:.2f} m/s = {:.2f} mph'.format(windspeed, windspeed*2.237))

# GPIO.cleanup()