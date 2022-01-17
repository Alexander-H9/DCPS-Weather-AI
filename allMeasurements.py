import multiprocessing
import readDataFromInflux
from numpy import True_
import windSpeedMeasurement
import ultrasonicMeasurement
import degreeMeasurement
import time

if __name__ == '__main__':

    # shared memmorey array for process communication
    measurements = multiprocessing.Array('f', 4)
    # initialise the array with 0
    for idx in range(len(measurements)):
        measurements[idx] = 0.0
        
    pVel = multiprocessing.Process(target=windSpeedMeasurement.windM, args=(measurements,1))
    pDeg = multiprocessing.Process(target=degreeMeasurement.degM, args=(measurements, 1))
    pVolt = multiprocessing.Process(target=ultrasonicMeasurement.voltM, args=(measurements,1))

    pList =[pVel, pDeg, pVolt]
    print("starting measurement processes")
    for p in pList:
        p.start()

    measureStart = time.time()
    try:
        while True:
            # if all(measurements) != 0.0:
            print("\nwrite the measurements to influxdb: ", measurements[0], ", ", measurements[1], ", ", measurements[2], ", ", measurements[3], "\n")
            readDataFromInflux.sendToInfluxDB("windMeasureAI3", measurements[0], measurements[1], measurements[2], measurements[3])
            time.sleep(1)   
    except KeyboardInterrupt:
        pass

    for p in pList:
        p.join()

    print("done")

    # windMeasureAI erste Messung mit time_interval = 2
    # windMeasureAI3 zweite Messung mit time_interval = 10, 2 min pro Windsftufe (Windstufen: 0-3)