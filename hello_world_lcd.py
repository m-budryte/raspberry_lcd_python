#!/usr/bin/env python

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

input_value = ""

while input_value != "exit":
    input_value = raw_input("Enter your msg: ") 

    mylcd.lcd_display_string(input_value, 1,5)
    
    sleep(1)

mylcd.lcd_clear()

