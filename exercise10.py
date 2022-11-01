#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:34:23 2022

@author: thomas
"""
import sys
fileName = input('Enter the name of the file:')

country = input('Enter the name of the country:')
try:
    fhand = open('/Users/thomas/Downloads/'+fileName)
except:
    print('File cannot be opened:', fileName)
    sys.exit()
    
contents = fhand.read()

for row in fhand:
    if country == row[1]:
        print(row)


