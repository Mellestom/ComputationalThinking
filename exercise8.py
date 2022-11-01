#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:27:43 2022

@author: thomas
"""

rows = int(input('Enter the number of rows for your first pyramid:\t'))
height = int(input('Enter the height of your triangle:\t'))

currency_notation = "{:.2f}".format(rows)
star = '*'
lines = 0
while lines <= rows:
    stars = round(rows / 2)
    lines+=1
    if lines <= stars:
        print(star)
        star = star+'*'
        secondstar = star
        
    else:
        secondstar = secondstar.replace('*','',1)
        print(secondstar)
