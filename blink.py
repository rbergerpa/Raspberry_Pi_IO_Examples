#!/usr//bin/python
import RPi.GPIO as GPIO
import time

LED_PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while (True):
    GPIO.output(LED_PIN, True)
    time.sleep(0.5)
    GPIO.output(LED_PIN, False)
    time.sleep(0.5)
