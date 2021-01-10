#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

fontdata1 = [      
        [ 0b01110, 
          0b01110, 
          0b00100, 
          0b00100, 
          0b00100, 
          0b00100, 
          0b11111, 
          0b11011 ],
        [ 0b01110, 
          0b01110, 
          0b00100, 
          0b00100, 
          0b00100, 
          0b00100, 
          0b11111, 
          0b11011 ],
        [ 0b01110, 
          0b01110, 
          0b00100, 
          0b00100, 
          0b00100, 
          0b00100, 
          0b11111, 
          0b11011 ],]

mylcd.lcd_load_custom_chars(fontdata1)
mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)
mylcd.lcd_write_char(2)
mylcd.lcd_write_char(4)

