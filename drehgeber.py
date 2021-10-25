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
list = ['LOW', 'LOW']

while True:
    sleep(0.1)
    if GPIO.input(channel):
        #print('Input was HIGH')
        list.append('HIGH')
    else:
        #print('Input was LOW')
        list.append('LOW')

    if len(list) > 2:
        list = list[1:]
    print(list)
    if list[0] == 'LOW' and list[1] == 'HIGH':
        k += 1
        #print(k, list)