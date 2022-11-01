#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:31:38 2022

@author: thomas
"""

import numpy as np

a = np.arange(1,101)
a = a.reshape(5,20)

b = np.arange(201,301)
b = b.reshape(5,20)

c = a + b


d = np.sum(a,axis=0).tolist()
e = np.sum(b,axis=0).tolist()

print(c)

print(d)
print(e)

a = a.T
b = b.T

f = np.diff(a)
print(f)

