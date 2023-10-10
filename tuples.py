#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:12:08 2023

@author: monika
"""

#conveniently used to swap variable values

# temp = x
# x= y
# y= temp

# or you can simply use "TUPLES" to "swap" values

# (x,y) = (y,x)



# Tuples can be used to return more than one value from a function

def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return (q,r)

(quot, rem) = quotient_and_remainder(4, 5)



# Manipulating Tuples

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

(small, large, words) = get_data(((1,"mine"), (3,"yours"), (5,"ours"), (7,"mine")))