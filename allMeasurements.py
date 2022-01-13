import multiprocessing
import readDataFromInflux
from numpy import True_
import windSpeedMeasurement
# import ultrasonicMeasurement
import degreeMeasurement
from time import sleep
import time

if __name__ == '__main__':

    # shared memmorey array for process communication
    measurements = multiprocessing.Array('f', 4)
    # initialise the array with 0
    for idx in range(len(measurements)):
        measurements[idx] = 0.0
        
    pVel = multiprocessing.Process(target=windSpeedMeasurement.windM, args=(measurements,1))
    pDeg = multiprocessing.Process(target=degreeMeasurement.degM, args=(measurements, 1))
    # pVolt = multiprocessing.Process(target=ultrasonicMeasurement.voltM, args=(measurements,1))

    pList =[pVel, pDeg]
    print("starting measurement processes")
    for p in pList:
        p.start()

    measureStart = time.time()
    try:
        while True:
            if measureStart + 5 < time.time():
                print("\nReset the measurements due to timeout.")
                print("The values of the measurements:[", measurements[0], ",", measurements[1], ",", measurements[2], ",", measurements[3],"]")
                print("will be set to 0.0\n")
                for idx in range(len(measurements)):
                    measurements[idx] = 0.0
                measureStart = time.time()

            if all(measurements) != 0.0:
                print("\nwrite the measurements to influxdb: ", measurements[0], ", ", measurements[1], ", ", measurements[2], ", ", measurements[3], "\n")
                readDataFromInflux.sendToInfluxDB("dataTest6", measurements[0], measurements[1], measurements[2], measurements[3])
                for idx in range(len(measurements)):
                    measurements[idx] = 0.0
                time.sleep(1)   # send in intervall of 1 second or more
    except KeyboardInterrupt:
        pass

    for p in pList:
        p.join()

    print("done")