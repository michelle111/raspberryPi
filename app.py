# success
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from flask import Flask, render_template


# 設定GPIO相關設定
# 車子部分
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


# 風扇部分
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

p12 = GPIO.PWM(12, 38)

app = Flask(__name__)

# 連結到樹梅派的時候會打開網頁
@app.route('/')
def index():
    return render_template('index.html')

# 定義三種風速


def fanL():

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    p12.start(20)

    p12.ChangeFrequency(500)


def fanM():

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    p12.start(60)

    p12.ChangeFrequency(500)


def fanH():

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    p12.start(90)

    p12.ChangeFrequency(500)

# 由dht22取得溫度


def getDHTdata():
    DHT22Sensor = Adafruit_DHT.DHT22
    DHTpin = 4
    hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp, 1)
    return temp

# 對於不同溫度執行不同的風速


def DHTdata():
    i = 1
    while i == 1:
        temp = getDHTdata()
        print("temp=%f" % temp)

        if temp < 20:
            fanL()

        elif temp >= 21 and temp < 23.2:
            fanM()

        elif temp > 23.5:
            fanH()

        time.sleep(1)


# 車子行進方向設定
# 左轉
@app.route('/left', methods=['GET', 'POST'])
def left():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    DHTdata()
    return render_template('index.html')
# 每次下完指令，就會再回到首頁，下同


@app.route("/back", methods=['GET', 'POST'])
# 後退
def back():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    # DHTdata()
    return render_template('index.html')


# 停止
@app.route("/stop", methods=['GET', 'POST'])
def stop():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    # DHTdata()
    return render_template('index.html')


# 前進
@app.route("/forward", methods=['GET', 'POST'])
def forward():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    # DHTdata()

    return render_template('index.html')

# 右轉
@app.route("/right", methods=['GET', 'POST'])
def right():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    # DHTdata()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
