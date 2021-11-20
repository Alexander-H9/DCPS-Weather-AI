#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO

class Sensor:
    def __init__(self):
        self.speed = 0
        self.zero_crossing = 0
        self.phase_1 = 0
        self.phase_2 = 0

sen = Sensor()

channel = 37        # gpio pin 26
channel2 = 36       # gpio pin 16
channel3 = 32       # gpio pin 12 zero crossing

def callback_ch1(channel):   
    print('Edge detected on channel %s'%channel)
    sen.phase_1 = GPIO.input(channel)
    sen.phase_2 = GPIO.input(channel2)
    sen.zero_crossing = GPIO.input(channel3)
    print("ch1: ", sen.phase_1, "ch2: ", sen.phase_2, "ch3: ", sen.zero_crossing)


def callback_ch2(channel2):
    print('Edge detected on channel %s'%channel2)
    sen.phase_1 = GPIO.input(channel)
    sen.phase_2 = GPIO.input(channel2)

    sen.zero_crossing = GPIO.input(channel3)
    print("ch1: ", sen.phase_1, "ch2: ", sen.phase_2, "ch3: ", sen.zero_crossing)

def callback_ch3(channel3):
    print('################################################ zero crossingEdge detected on channel %s'%channel3)
    sen.phase_1 = GPIO.input(channel)
    sen.phase_2 = GPIO.input(channel2)
    sen.zero_crossing = GPIO.input(channel3)
    print("ch1: ", sen.phase_1, "ch2: ", sen.phase_2, "ch3: ", sen.zero_crossing)

GPIO.setmode(GPIO.BOARD)

#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.RISING, callback=callback_ch1)

GPIO.setup(channel2, GPIO.IN)
GPIO.add_event_detect(channel2, GPIO.RISING, callback=callback_ch2)

GPIO.setup(channel3, GPIO.IN)
GPIO.add_event_detect(channel3, GPIO.RISING, callback=callback_ch3)


while True:
    pass