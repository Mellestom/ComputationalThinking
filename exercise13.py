#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:30:27 2022

@author: thomas
"""

file = open('mbox-short.txt')

content = file.readlines()

sendlines = 'From'

if sendlines in content:
    print(sendlines)