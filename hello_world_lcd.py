#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

input_value = ""

while input_value != "exit":
    input_value = raw_input("Enter your msg: ") 

    if input_value == "balance":
        mylcd.lcd_display_string("Your Revolut balance U+00A30.00", 1)
        mylcd.lcd_display_string("Your Barc balance is U+00A30.00", 2)

    sleep(5)

    mylcd.lcd_clear()


