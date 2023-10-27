#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 23:36:15 2023

@author: monika
"""

#generate subsets

def genSubsets(L):
    #print("***********CALLED FOR**************", L)
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    #print("smaller====>", smaller)
    extra = L[-1:] # create a list of just last element
    print("extra====>", extra)
    print("===========")
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
        print("new=", new)
    #print("for L =========Returning===========", L,smaller + new)
    print()
    print(smaller + new)
    return smaller+new  # combine those with last element and those without

test = [1,2,3,4]

super = genSubsets(test)
