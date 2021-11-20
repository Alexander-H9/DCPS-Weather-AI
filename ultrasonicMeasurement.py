import PCF8591
from time import sleep
from dbConnectionUltrasonic import *

db = InfluxDB()

adc = PCF8591
i2cAddress = 0x48   # ADC I2C-address
CH0 = 0x40          # define channel 0
CH1 = 0x41          # define channel 1
CH2 = 0x42          # define channel 2
CH3 = 0x43          # define channel 3

while True:
  # read channel 0
  CH0_val = adc.readADCvalue(i2cAddress, CH0)
  CH0_vol = adc.readADCvoltage(i2cAddress, CH0)
  # read channel 1
  CH1_val = adc.readADCvalue(i2cAddress, CH1)
  CH1_vol = adc.readADCvoltage(i2cAddress, CH1)
  # read channel 2
  CH2_val = adc.readADCvalue(i2cAddress, CH2)
  CH2_vol = adc.readADCvoltage(i2cAddress, CH2)
  # read channel 3
  CH3_val = adc.readADCvalue(i2cAddress, CH3)
  CH3_vol = adc.readADCvoltage(i2cAddress, CH3)

  # output channel reads
  print("CH0-Value: " + str(CH0_val))
  print("CH0-Voltage: " + str(CH0_vol) + " V")
  print("CH1-Value: " + str(CH1_val))
  print("CH1-Voltage: " + str(CH1_vol) + " V")
  print("CH2-Value: " + str(CH2_val))
  print("CH2-Voltage: " + str(CH2_vol) + " V")
  print("CH3-Value: " + str(CH3_val))
  print("CH3-Voltage: " + str(CH3_vol) + " V")
  print("-----------------------------------------------------")

  # send data to database
  db.sendToInfluxDB("ultrasonic2", CH0_vol, CH1_vol)

  # wait for 1 sec
  sleep(1)