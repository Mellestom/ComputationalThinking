#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:17:41 2022

@author: thomas
"""

file = open('names.txt')
content = file.readlines()


name = input('Enter a name to find: ')

namedict = {}
count=0
for line in content:
    line = line.rstrip()
    count+=1
    key = line
    val = count
    namedict[key] = val
    
count = str(count)

print('There are this many names in the file:' + count)

if namedict.get(name)!= None:
    print('Found')
else:
    print('Not Found')
    