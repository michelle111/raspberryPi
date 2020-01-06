import RPi.GPIO as gpio
import time

#led = 2
trig = 29
echo = 31


#gpio.setup(led, gpio.OUT)
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.output(trig, gpio.LOW)


def distance():
    gpio.output(trig, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(trig, gpio.LOW)

    start_time = time.time()
    end_time = 0
    while gpio.input(echo) == gpio.LOW:
        start_time = time.time()

    while gpio.input(echo) == gpio.HIGH:
        end_time = time.time()

    echo_time = end_time - start_time
    d = echo_time * 343
    d = d / 2
    return d * 100


try:
    while True:
        dis = distance()
        print('{0:.1f}cm'.format(distance()))
        # if dis < 10:
        # for i in range(3):
        #gpio.output(led, gpio.HIGH)
        # time.sleep(0.5)
        #gpio.output(led, gpio.LOW)
        # time.sleep(0.5)
        # time.sleep(2)
except KeyboardInterrupt:
    pass
gpio.cleanup()
