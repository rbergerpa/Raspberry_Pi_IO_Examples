#!/usr//bin/python
import time
from Adafruit_LED_Backpack import SevenSegment
from ds18b20 import DS18B20

DEVICE = '28-000003cb57a4'
BRIGHTNESS=4  # 15 = max

display = SevenSegment.SevenSegment(address=0x71)
display.begin()
display.set_brightness(BRIGHTNESS)

sensor = DS18B20(DEVICE)

while True:
    temperature = sensor.read_fahrenheit()
    display.clear()
    display.print_number_str('%d ' % round(temperature))
    display.set_digit_raw(3, 0x63) # degree symbol
    display.write_display()
    time.sleep(10.0)


