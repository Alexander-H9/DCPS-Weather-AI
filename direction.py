#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO

class Sensor:
    def __init__(self):
        self.zero_crossing = 0
        self.phase_1 = 0
        self.phase_2 = 0

sen = Sensor()

channel1 = 37       # gpio pin 26
channel2 = 36       # gpio pin 16
channel3 = 32       # gpio pin 12 zero crossing

def callback_ch1(channel):   

    print('Edge detected on pin %s'%channel1)
    sen.phase_1 = GPIO.input(channel1)
    sen.phase_2 = GPIO.input(channel2)
    sen.zero_crossing = GPIO.input(channel3)

    if sen.phase_2 == 0:
        print("ch2 = 0")
    if sen.phase_2 == 1:
        print("ch2 = 1")
    # print("ch1: ", sen.phdeg = calculate_degree(count)
        # print("deg: ", deg)O.input(channel3)
    print("ch1: ", sen.phase_1, "ch2: ", sen.phase_2, "ch3: ", sen.zero_crossing)

def callback_ch3(channel3):
    # print('################################################ zero crossingEdge detected on pin %s'%channel3)
    # sen.phase_1 = GPIO.input(channel1)
    # sen.phase_2 = GPIO.input(channel2)
    # sen.zero_crossing = GPIO.input(channel3)
    # print("ch1: ", sen.phase_1, "ch2: ", sen.phase_2, "ch3: ", sen.zero_crossing)
    pass


def calculate_degree(counter):
    deg = counter/1.388
    return int(deg)

GPIO.setmode(GPIO.BOARD)


GPIO.setup(channel1, GPIO.IN)
#GPIO.add_event_detect(channel, GPIO.RISING, callback=callback_ch1)

GPIO.setup(channel2, GPIO.IN)
#GPIO.add_event_detect(channel2, GPIO.RISING, callback=callback_ch2)

GPIO.setup(channel3, GPIO.IN)
#GPIO.add_event_detect(channel3, GPIO.RISING, callback=callback_ch3)

phase_0 = GPIO.input(channel1)
count = 0
dir = 0
i = 0
deg = 0
trigger = 0

while True:
    sen.zero_crossing = GPIO.input(channel3)
    sen.phase_1 = GPIO.input(channel1)

    if sen.zero_crossing == 1 and trigger == 0:
        trigger = 1
        if count > 500 or count < -500:
            count = 500
        # deg = calculate_degree(count)
        # print("deg: ", deg)
        
        count = 0


    if sen.zero_crossing == 0:  
        trigger = 0
    
    if sen.phase_1 == 1 and phase_0 == 0:
        i += 1
        
        sen.phase_2 = GPIO.input(channel2)
        
        if sen.phase_2 == 0:
            dir = 0
            count += 1
        else:
            dir = 1
            count -= 1


    phase_0 = sen.phase_1
    

    if i > 10:
        #print("dir:", dir, i)
        #print("deg: ", calculate_degree(count))
        deg = calculate_degree(count)
        print("deg: ", deg)
        i = 0
        deg = calculate_degree(count)
        print("deg: ", deg)