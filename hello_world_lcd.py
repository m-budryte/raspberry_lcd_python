#!/usr/bin/env python

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

input_value = ""

while input_value != "exit":
    input_value = raw_input("Enter your value: ") 

    mylcd.lcd_display_string(input_value, 1)
    
    sleep(5)

mylcd.lcd_clear()

