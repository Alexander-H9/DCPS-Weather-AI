#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO

channel = 37


GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(channel, GPIO.IN)
#GPIO.setup(channel, GPIO.IN)

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

k = 0

while True:
    sleep(0.1)
    if GPIO.input(channel):
        print('Input was HIGH')
        k += 1
    else:
        print('Input was LOW')
    print(k)


    