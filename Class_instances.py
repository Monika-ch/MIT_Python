#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:46:02 2023

@author: monika
"""

# Class Instances:
    
    
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    '''   
    def getX(self):
        return x        # throws error: name 'x' is not defined
    
    def getY(self):
        return y        # throws error: name 'y' is not defined
    '''
        
    def distance(self, other):
        #print("self.x-other.x:",self.x-other.x)
        x_diff_sq = (self.x - other.x)**2
        #print("x_diff_sq:", x_diff_sq)
        
        #print("self.y-other.y:",self.y-other.y)
        y_diff_sq = (self.y - other.y)**2
        #print("y_diff_sq:", y_diff_sq)
        
        return (x_diff_sq + y_diff_sq)**0.5
    
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    
    
c = Coordinate(3, 4) #c.x = 3 #c.y = 4
origin = Coordinate(0, 0) #origin.x = 0 #origin.y = 0
#origin = Coordinate(5, 10) 
print(c.x) # prints 3
print(origin.x)  # prints 0 
print(c.distance(origin)) # equivalent to print(Coordinate.distance(c, origin))
print(Coordinate.distance(c, origin))

print(c)
print(type(c))
print(Coordinate, type(Coordinate))
print(isinstance(c, Coordinate)) #is c an instance of Coordinate

#substract the self x,y and other x,y coordinates using __sub__ python built in method for class instances
c = Coordinate(5, 6) 
origin = Coordinate(2, 4)
foo = c - origin
print(foo)