#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

full_square = [ 0b11111, 
          0b11111, 
          0b11111, 
          0b11111, 
          0b11111, 
          0b11111, 
          0b11111, 
          0b11111 ]

empty_square = [ 0b00000, 
          0b00000, 
          0b00000,
          0b00000,
          0b00000, 
          0b00000, 
          0b00000,
          0b00000 ]

top_row = [full_square, full_square, full_square, full_square, full_square, full_square]
middle_row = [full_square, full_square, full_square, full_square, full_square, full_square]
bottom_row = [full_square, full_square, full_square, full_square, full_square, full_square]

mylcd.lcd_load_custom_chars(top_row)

mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)

mylcd.lcd_load_custom_chars(middle_row)


mylcd.lcd_write(0xC0)
mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)

sleep(5)

mylcd.lcd_clear()



