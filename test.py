#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:29:29 2023

@author: monika
"""

#Functions and examples

# example 1
def square(n):
    '''
    n: int or float.
    '''
    return n**2
square(5)

# example 2
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return (a*(x**2)) + (b*x) + c
evalQuadratic(3, 4, 5, 10)

# example 3
def square2(x):
    '''
    x: int or float.
    '''
    print("I am getting squared", x**2)
print("square2: sq =", square2(5))


#### LOCAL AND GLOBAL SCOPE (run each of the following case to undersatand the difference in the answer)

# example 4
def f(y):
    x=1
    x+=1
    print("f(y) =", x)
    
x=5
f(x)
print("global scope, f(y) =",x)

# example 5
def g(y):
    print(x)
    print(x+1)
    
x=5
g(x)
print(x)

# example 6 : following case gives error
'''
def h(y):
    x=x+1
    
x=5
h(x)
print(x)
'''

##### function defined inside aother function
def g(x):
    def h():
        x="abc"
    x=x+1
    print("in g(x): x=", x)
    h()
    return x

x=3