#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:14:56 2022

@author: thomas
"""

n = int(input('Enter an integer greater than or equal to one and less than or equal to one million:'))

if 1000000 >= n >= 1 == True:
    
    if n % 2 == 0:
        
        if (500000 >= n >= 2) == True:
            print('Not odd')
            
        elif (750000 >= n >= 500001) == True:
            print('Not odd too')
            
        elif (n > 750000) == True:
            print('Absolutely not odd')
            
        else:
            print('did not work')
    else:
        print('Odd')
else:
    print('invalid number')
    