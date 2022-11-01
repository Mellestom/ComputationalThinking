# -*- coding: utf-8 -*-
"""
Exercise 21 - Car class, and three car instances

"""

# Car class
class Car():
    
    
# main

    def __init__(self,color,miles):
        
        self.color = color
        self.miles = miles

    def __str__(self):
     
        return 'a {self.color} car with {self.miles} miles'.format(self=self)

    def paint(self,color):
        self.color = color

    def addMiles(self,miles):
        self.miles +=10000
# Create three car objects
    
blue = Car('blue',20000)
green = Car('green',13000)
red = Car('red',30000)



# Display object's information using __str__ method of class

print(blue)
print(green)
print(red)


# Change all car colors to black using the paint method and display
  
blue.paint('black')
green.paint('black')
red.paint('black')

print(blue)
print(green)
print(red)
    
# Change each car color back using color property and display


# Add 10,000 miles to the green car using addMiles method and display
    
green.addMiles(13000)
print(green)