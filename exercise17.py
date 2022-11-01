#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:20:36 2022

@author: thomas
"""
import turtle
  
# creating turtle pen
t = turtle.Turtle()
  
# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon between 3 and 15: "))
  
if 3 > n > 15:
    print('Error')
# taking input for the length of the sides of the polygon
  
color = input('Enter the color of the polygon: ')

turtle.pencolor(color)
for _ in range(n):
    turtle.forward(75)
    turtle.right(360 / n)

