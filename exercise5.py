#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:34:49 2022

@author: thomas
"""
from math import pi
from math import pow

diameter = float(input('Enter the diameter of the circle:',))

area = pow((diameter/2),2)*pi
area = round(area,4)
area_str = '{0:.6f}'.format(area)
print('The area of the circle is:', area_str)


second = int(input('Enter the number of seconds already passed:',))
minute = second/60

time = int(minute//60)
time2 = int(minute%60)

str_time = str(time)
str_time2 = str(time2)

print('The time of the day is:',str_time+':'+str_time2)