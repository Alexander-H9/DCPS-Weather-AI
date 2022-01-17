from influxdb import InfluxDBClient
import numpy as np
import datetime

def sendToInfluxDB(measurement_name, v1, v2, vel, deg):

    # take a timestamp for this measurement
    time = datetime.datetime.utcnow()

    # format the data as a single measurement for influx
    body = [
                {
            "measurement": measurement_name,
            "time": time,
            "fields": {
                "v1": v1,
                "v2": v2,
                "vel": vel,
                "deg": deg
            }
        }
    ]

    # write the measurement
    ifclient.write_points(body)


def readFromInflux():

    print(ifclient.get_list_database())

    ifclient.switch_database('home')
    dataSet = (ifclient.query('select v1,v2,vel,deg from finalTest01;'))
    # return dataSet
    v1 = []
    v2 = []
    vel = []
    deg = []
    for element in dataSet:
        if type(element) == list:
            for value in element:
                v1.append(value['v1'])
                v2.append(value['v2'])
                vel.append(value['vel'])
                deg.append(value['deg'])

    return v1,v2,vel,deg


# # get/create the data
# sd_noise = 0.5                                                            # noise power (=standard deviation)
# v1 = np.arange(-3,7,1)
# v1 = v1 + np.random.normal(0,sd_noise,v1.shape)
# v2 = np.arange(-3,7,1)
# v2 = v2 + np.random.normal(0,sd_noise,v2.shape)
# vel = np.arange(-11,9,2)
# vel = vel + np.random.normal(0,sd_noise,vel.shape)
# deg = np.arange(0,360,36)
# deg = deg + np.random.normal(0,sd_noise,deg.shape)

# influx configuration
ifuser = "grafana"
ifpass = "dcpsaamr"
ifdb   = "home"
ifhost = "127.0.0.1"
ifport = 8086

# connect to influx
global ifclient
ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

# for idx,value in enumerate(v1):
#     sendToInfluxDB("dataTest6", list(v1)[idx], list(v2)[idx], list(vel)[idx], list(deg)[idx])

# print(readFromInflux())