import RPi.GPIO as GPIO
import time
from flask import Flask, render_template


# 設定GPIO相關設定
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

# led = 2
trigger_pin = 29
echo_pin = 31

# gpio.setmode(gpio.BCM)

# gpio.setup(led, gpio.OUT)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.output(trigger_pin, GPIO.LOW)


# 不明究理的地方
# 主要參考http://www.cnblogs.com/ttssrs/p/4890635.html
# 方向的輸出高低電壓可能還要在做修改

app = Flask(__name__)

# 連結到樹梅派的時候會打開網頁
@app.route('/')
def index():
    return render_template('index.html')


def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin, False)


def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1


def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 5000)
    start = time.time()
    wait_for_echo(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340 * 100 / 2

    return (distance_cm)


# 前進
@app.route('/forward', methods=['GET', 'POST'])
def forward():

    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    # distance()
    return render_template('index.html')
# 每次下完指令，就會再回到首頁，下同


@app.route("/left", methods=['GET', 'POST'])
# 左轉
def left():

    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    # distance()
    return render_template('index.html')

# 停止
@app.route("/stop", methods=['GET', 'POST'])
def stop():

    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    # distance()
    return render_template('index.html')

# 右轉
@app.route("/right", methods=['GET', 'POST'])
def right():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    distance()

    return render_template('index.html')

# 後退
@app.route("/back", methods=['GET', 'POST'])
def back():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    # distance()

    return render_template('index.html')


 def distance():
    i = 1
    while i == 1:
        dis = get_distance()
        print("cm=%f" % dis)
        if dis < 35:
            stop()
        time.sleep(1)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# try:
#     while True:
#         dis = distance()
#         print('{0:.1f}cm'.format(distance()))
#         if dis < 30:
#             stop()

# except KeyboardInterrupt:
#     pass
# gpio.cleanup()
