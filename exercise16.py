#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:21:27 2022

@author: thomas
"""
# Part 1
myTuple = ('Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A')
sortTuple = sorted(myTuple)
print(sortTuple)
sortTuple = tuple(sortTuple)
print(sortTuple)

# Part 2
first = sortTuple[0]
last = sortTuple[-1]

print(first)
print(last)



# Part 3
myTuple2 = ([1,2], ['x', 'y']) 
y = list(myTuple2)

y[0] = [99,2]
y[1] = ['t','y']

myTuple2 = tuple(y)
print(myTuple2)
