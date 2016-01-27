#!/usr//bin/python
import RPi.GPIO as GPIO
import time

RED_LED = 26
GREEN_LED = 19
BLUE_LED = 13

def delay():
    time.sleep(1.0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

while (True):
    GPIO.output(GREEN_LED, False)
    GPIO.output(BLUE_LED, False)
    GPIO.output(RED_LED, True)
    delay()

    GPIO.output(GREEN_LED, True)
    delay()

    GPIO.output(RED_LED, False)
    delay()

    GPIO.output(BLUE_LED, True)
    delay()

    GPIO.output(GREEN_LED, False)
    delay()

    GPIO.output(RED_LED, True)
    delay()

    GPIO.output(GREEN_LED, True)
    delay()
