#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:53:41 2023

@author: monika
"""

# Class Exercise


#1 What does the code print out? 
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()

#2 What does the code print out? 
class Clock(object):
    def __init__(self, time):
	    self.time = time
    def print_time(self, time):
	    print(time)

clock = Clock('5:30')
clock.print_time('10:30')

#3 What does the code print out? 
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
# boston_clock and paris_clock are different objects



# Code:

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    
    # remove the docstring to see the complete code
    '''
    def getX(self):
        return x 
    def getY(self):
        return y
    '''

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

#remove above docstring before solving the following questions

#4 print out? 
w1 = Weird(X, Y)
print(w1.getX()) #error

#5 print out? 
print(w1.getY()) #error

#6 print out? 
w2 = Wild(X, Y)
print(w2.getX()) # returns 7

#7 print out? 
print(w2.getY()) # returns 8

#8 print out? 
w3 = Wild(17, 18)
print(w3.getX())

#9 print out? 
print(w3.getY())

#10 print out? 
w4 = Wild(X, 18)
print(w4.getX())

#11 print out? 
print(w4.getY())

#12 print out? 
X = w4.getX() + w3.getX() + w2.getX()
print(X)

#13 print out?
print(w4.getX())

#14 print out?
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)

#15 print out?  
print(w2.getY())

#16 print out?  
#17 print out?  
#18 print out?  
#19 print out?  
#20 print out?  

