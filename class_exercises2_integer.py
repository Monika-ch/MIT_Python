#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:36:56 2023

@author: monika
"""

# Class Exercise Integer Coordinate

#Problem 1
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    
    def __eq__(self, other):
        if self.getX() == other.getX():
            return self.getY() == other.getY()
        return False        
        
    def __repr__(self):
        return "Coordinate(" + str(self.getX()) + "," + str(self.getY()) + ")"
    
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
# Your task is to define the following two methods for the Coordinate class:

# 1. Add an __eq__ method that returns True if coordinates refer to same point in
#       the plane (i.e., have the same x and y coordinate).

# 2. Define __repr__, a special method that returns a string that looks like a 
#       valid Python expression that could be used to recreate an object with the
#       same value. In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.


a = Coordinate(5, 10)
print("a =", a)
b = Coordinate(5, 10) 
print("b =", b)
print("a.__eq__(b) =", a.__eq__(b))

c = Coordinate(10, 10) 
print("c =", c)
print("a.__eq__(c) =", a.__eq__(c))

d = Coordinate(10, 5) 
print("d =", d)
print("a.__eq__(d) =", a.__eq__(d))

print("c.__eq__(d) =", c.__eq__(d))

#Try the following in the console:
a #Outputs: Coordinate(5,10)
eval(repr(a)) #Outputs: Coordinate(5,10)
eval(repr(a))==a #Outputs: True




#Problem 2
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def intersect(self, other):
        """Assumes other is an intSet
           Returns a new intSet containing elements that appear in both sets."""
        # # Initialize a new intSet    
        commonValueSet = intSet()
        # Go through the values in this set
        for val in self.vals:
            # Check if each value is a member of the other set    
            if other.member(val):
                commonValueSet.insert(val)
        return commonValueSet
            
    def __len__(self):
        """Returns the number of elements in self"""
        return len(self.vals)

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    
'''
Your task is to define the following two methods for the intSet class:

Define an intersect method that returns a new intSet containing elements that
appear in both sets. In other words,
s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. 
Think carefully - what should happen if s1 and s2 have no elements in common?

Add the appropriate method(s) so that len(s) returns the number of elements in s.

Hint: look through the Python docs to figure out what you'll need to solve this problem.
'''