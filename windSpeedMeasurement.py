#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import math
from dbConnectionWindSpeed import *

def windM(measurements, x):

	# gpio pin 6
	pin = 31    
	time_interval = 3 		# intervall of sending data to influx in seconds   

	def callbackPin(pin):
		print("Umdrehung")

	# Set up GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.IN)
	GPIO.add_event_detect(pin, GPIO.RISING, callback=callbackPin)

	db = InfluxDB()


	# Anamometer vane diameter (set to the value for your cup-to-cup in mm)
	vane_diameter = float(130)			# durchmesser von cup-mittelpunkt zu cup-mittelpunkt

	# Calculate vane circumference in metres (umfang)
	vane_circ = float(vane_diameter/1000)*math.pi

	# Set an anamometer factor to account for inefficiency (value is a guess)
	afactor = float(2.5)		# 0.95

	# Start measuring wind speed
	# print('Measuring wind speed...')

	# Define variables rotations and trigger (trigger = 1 if sensor triggered)
	rotations = 0
	trigger = 0
	firstRotation = True

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

			time.sleep(0.01)

		else:
			# 10 seconds has now finished. But if sensor triggered at start and did not move,
			# rotations value will be 1, which is wrong, so 
			if rotations==1 and sensorstart==1:
				rotations = 0

			# fix start problem
			if firstRotation == True:
				rotations = 0
				firstRotation = False

			# Calculate
			rots_per_second = float(rotations/time_interval)
			windspeed = float((rots_per_second)*vane_circ*afactor)

			# print('{:.0f} rotations = {:.2f} rotations/second'.format(rotations, rotations/time_interval))
			# print('Windspeed is {:.2f} m/s = '.format(windspeed))

			# setup the time for the next 10 seconds
			endtime = time.time() + time_interval

			# send data to database
			if x == 0:
				db.sendToInfluxDB("windSpeed", windspeed)
			elif x == 1:
				measurements[2] = windspeed
				# print("vel=", windspeed)
			
			rotations = 0
			
