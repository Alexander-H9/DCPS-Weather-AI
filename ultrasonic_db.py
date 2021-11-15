#!/usr/bin/env python

import datetime
from influxdb import InfluxDBClient

from random import randint
from time import sleep

class InfluxDB():

    def __init__(self):
        pass

    def sendToInfluxDB(self, name, CH0, CH1):

        # influx configuration
        ifuser = "grafana"
        ifpass = "dcpsaamr"
        ifdb   = "home"
        ifhost = "127.0.0.1"
        ifport = 8086
        measurement_name = name

        # take a timestamp for this measurement
        time = datetime.datetime.utcnow()

        # format the data as a single measurement for influx
        body = [
            {
                "measurement": measurement_name,
                "time": time,
                "fields": {
                    "CH0": CH0,
                    "CH1": CH1
                }
            }
        ]

        # connect to influx
        ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

        # write the measurement
        ifclient.write_points(body)

# while True:
#     db = InfluxDB()
#     rand = randint(0,360)
#     db.sendToInfluxDB("anemometerTest", rand)
#     print("wrote: ", rand)
#     sleep(1)