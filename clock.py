#!/usr//bin/python
import time
from Adafruit_LED_Backpack import SevenSegment

display = SevenSegment.SevenSegment(address=0x70)
display.begin()
colon = False

# Turn the upper LED of the left colon of the Adafruit 1.2" display on or off
def set_pm(pm_on):
    if pm_on:
        display.buffer[4] |= 0x04
    else:
        display.buffer[4] &= (~0x04) & 0xFF

while True:
    local_time = time.localtime()
    time_str = time.strftime("%-I%M", local_time)
    pm = local_time.tm_hour > 12
    colon = ~colon

    display.clear()
    display.print_number_str(time_str)
    display.set_colon(colon)
    set_pm(pm)
    display.write_display()

    time.sleep(1.0)
