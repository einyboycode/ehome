#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import requests

apiurl = " http://api.yeelink.net/v1.0/device/7909/sensor/12548/datapoints"
header =  {'U-ApiKey':'f790aa8e585cc5ce0cda6015a6563cec'}

GPIO.setmode(GPIO.BOARD)
# need to set up every channel which are using as an input or an output
GPIO.setup(11, GPIO.OUT)

while True:
    r = requests.get(apiurl, headers=header);
    print(t.text)
    led = r.json
    if led["value"]==1:
    	GPIO.output(11, GPIO.LOW)
    else:
    	GPIO.output(11, GPIO.HIGH)
    time.sleep(5)
