import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

p13 = GPIO.PWM(13, 50)
p12 = GPIO.PWM(12, 38)

p13.start(50)
p12.start(0.5)
time.sleep(1)


def fanL():


p13.stop()
p12.stop()
GPIO.cleanup()

p13 = GPIO.PWM(13, 50)
p12 = GPIO.PWM(12, 38)

p13.start(20)
p12.start(0.5)
time.sleep(1)

p13.ChangeFrequency(500)
p12.ChangeFrequency(1)
time.sleep(1000)


def fanM():

    GPIO.cleanup()

    p13 = GPIO.PWM(13, 50)
    p12 = GPIO.PWM(12, 38)

    p13.start(60)
    p12.start(0.5)
    time.sleep(1)

    p13.ChangeFrequency(500)
    p12.ChangeFrequency(1)
    time.sleep(1000)


def fanH():

    GPIO.cleanup()

    p13 = GPIO.PWM(13, 50)
    p12 = GPIO.PWM(12, 38)

    p13.start(90)
    p12.start(0.5)
    time.sleep(1)

    p13.ChangeFrequency(500)
    p12.ChangeFrequency(1)
    time.sleep(1000)


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

        if temp < 20:
            fanL()

        else if temp >= 21 & temp < 23:
            fanM()

        else if temp > 25:
            fanH()

        time.sleep(1)


DHTdata()
