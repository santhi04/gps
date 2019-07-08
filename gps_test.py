impoprt os
import time
import serial
import string 
import pynmea2

while True:
     port="/dev/ttyAMAO"
     ser=serial.Serial(port,baudrate=9600,timeout=0.5)
     dataout=pynmea2.NMEAStreamReader()
     newdata=ser.readline()
     print ("get latitude and longitude")
     if newdata[0:6] =="$GPGGA":
        newmsg=pynmea2.parse(newdata)
  	lat=newmsg.latitude
 	print(lat)
  	lng=newmsg.longitude
  	print(lng)
  	time.sleep(10)
     
