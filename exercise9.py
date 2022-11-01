#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:17:28 2022

@author: thomas
"""

word1 = input('Enter CHORUS   ')

word1 = word1.lower()
word1 = word1.replace('chor','')

print(word1)

word2 = input('Enter d i n o s a u r     ')

word2 = word2.replace(' ','')
word2 = word2.replace('dino','')
print(word2)

word3 = input('What theme is a string?')
word3 = word2+word1
word3 = word3.replace('What',' ')
word3 = word3.replace('me',' ')
word3 = word3.replace('isstring',' ')
stringthe = word3[3:4]
word3 = word3.replace(' ','')
print(stringthe+word2+word1)


word3 = word2+word1

print(word3)

word4 = word2+word1
word4 = word4.replace('What',' ')
word4 = word4.replace('me',' ')
word4 = word4.replace('isstring',' ')
stringthe = word4[3:4]
word4 = word4.replace(' ','')
print(stringthe+word2+word1)
