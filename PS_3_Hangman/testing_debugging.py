#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:22:55 2023

@author: monika
"""

#debugging and testing

def isPal(x):
    assert type(x) == list
    temp = x[:]
    print('before reverse:', temp, x)
    temp.reverse()
    print('after reverse:', temp, x)
    if temp == x:
        return True
    else:
        return False
    
def silly(n):
    result=[]
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
    