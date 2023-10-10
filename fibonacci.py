#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:51:03 2023

@author: monika
"""

# FIBONACCI

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
    
    
    
#FIBONACCI MEMOIZATION with dictionary

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}


arg = 40
print("")
print("using fib")
print(fib(arg))
print("")
print("using fib_efficient")
print(fib_efficient(arg, d))