#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

input_value = ""

while input_value != "exit":
    input_value = raw_input("Enter your msg: ") 

    fontdata1 = [      
            [ 0b00010, 
            0b00100, 
            0b01000, 
            0b10000, 
            0b01000, 
            0b00100, 
            0b00010, 
            0b00000 ],
    ]

    mylcd.lcd_load_custom_chars(fontdata1)
    mylcd.lcd_write(0x80)
    mylcd.lcd_write_char(0)

    if input_value == "balance":
        mylcd.lcd_display_string("Your balance is ",  1)
        

    sleep(5)

    mylcd.lcd_clear()


