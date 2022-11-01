#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:41:54 2022

@author: thomas
"""
from PIL import Image, ImageEnhance


img = Image.open('sunflower.jpg')

def grey(img):
    img = Image.open('sunflower.jpg').convert('L')
    img.save('image.png')
    img.show()
    
def bright(img):
    enhancer = ImageEnhance.Brightness(img)

    factor = 1.5 #brightens the image
    img = enhancer.enhance(factor)
    img.save('Image.png')
    img.show()
    
def sharp(img):
    enhancer = ImageEnhance.Sharpness(img)

    factor = 30
    img = enhancer.enhance(factor)
    img.save('Image.png')
    img.show()
    
grey(img)
bright(img)
sharp(img)

