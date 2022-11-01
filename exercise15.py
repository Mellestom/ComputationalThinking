#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:40:36 2022

@author: thomas
"""

states = {}

def displaystates(states):
    for key,value in states.items():
        print(key+'           '+value[0]+'           '+value[3])
    

f = open('state_facts.csv')
content = f.readlines()

for line in content:
    line = line.rstrip()
    line = line.split(',')
    key = line[0]
    value = line[1:]
    states.update({key:value})
    
print('State            Capitol           Flower')
displaystates(states)