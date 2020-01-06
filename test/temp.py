# success
import Adafruit_DHT
import time


def getDHTdata():
    DHT22Sensor = Adafruit_DHT.DHT22
    DHTpin = 4
    hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp, 1)
    return temp


def DHTdata():
    i = 1
    while i == 1:
        temp = getDHTdata()
        print("temp=%f" % temp)
        # if dis < 35:
        # stop()
        time.sleep(0.5)


DHTdata()
