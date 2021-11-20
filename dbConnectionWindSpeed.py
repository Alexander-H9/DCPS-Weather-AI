#!/usr/bin/env python

import datetime
from influxdb import InfluxDBClient

from random import randint
from time import sleep

class InfluxDB():

    def __init__(self):
        pass

    def sendToInfluxDB(self, name, data):

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
                    "speed": data
                }
            }
        ]

        # connect to influx
        ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

        # write the measurement
        ifclient.write_points(body)