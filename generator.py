#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:53:12 2023

@author: monika
"""

# Generators

""" Generator is any procedure and method with a yield statement inside it.
Yield suspends the execution and returns a value.
Generators have associated with them a next() method.
It's built into the Python implementation. 
next() method starts or resumes the execution of a procedure.
When called for the next() method, it will go until it gets to the next yield() method,
in which case it will stop or suspend execution and return a value."""
def genTest():
    yield 1
    yield 2
    
foo = genTest()
print("foo.__next__() =", foo.__next__()) # prints 1
print("foo.__next__() =", foo.__next__()) # prints 2

# uncomment the below print statement and test it out
"""since there is no third yield so doing __next__ will throw StopIteration Error on third attempt"""
#print("foo.__next__() =", foo.__next__()) 

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        # notice: there's no way to exit out of this while loop.
        
fib = genFib()
print(fib)
print("fib.__next__() =", fib.__next__())
print("fib.__next__() =", fib.__next__())
print("fib.__next__() =", fib.__next__())
print("fib.__next__() =", fib.__next__())
print("fib.__next__() =", fib.__next__())
# notice: there's no way to exit out of this while loop.
print("fib.__next__() =", fib.__next__())
print("fib.__next__() =", fib.__next__())
print("fib.__next__() =", fib.__next__())


