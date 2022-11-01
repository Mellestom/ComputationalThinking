#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:30:43 2022

@author: thomas
"""

import random

sim = int(input('Enter how many simulations you would like to process'))
ran_sim = 0
money = 100
interest = 1
claim = 1
ruin = 0
n = 0
days = 0

while ran_sim < sim:
    ran_sim+=1
    money = 100
    days = 0
    while days < 500:
        p = random.randint(1,11)
        days+=1
        if money == 0:
            ruin+=1
        elif p <= 6:
            money = money - claim
        else:
            money = money + interest
            
            



p_ofruin = ruin/sim

print('The probability of ruin is', p_ofruin)


















