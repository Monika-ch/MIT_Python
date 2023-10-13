#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:07:51 2023

@author: monika
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""
    
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
        
    def insert(self, e):
        """Assume e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        """Assume e is an integer 
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assume e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found!')
        
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ""
        for e in self.vals:
            result = result + str(e) + ","
        return '{' + result[:-1] + '}'
    
s = intSet()
print("s =", s)
print("s.insert(3) =", s.insert(3))
s.insert(3)
s.insert(4)
print("s =", s) # removed the duplicate 3

print("s.member(3) =", s.member(3))
print("s.member(6) =", s.member(6))

print("s.remove(3) =", s.remove(3))
print("s.insert(6) =", s.insert(6))
print("s =", s) # 3 removed and 6 inserted

print("s.remove(3) =", s.remove(3)) # throws error: 3 not found!

