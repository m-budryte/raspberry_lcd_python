#!/usr/bin/env python

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

while True:
    input_value = raw_input("Enter your value: ") 

    mylcd.lcd_display_string(input_value, 1)
    sleep(1)

    mylcd.lcd_clear()
