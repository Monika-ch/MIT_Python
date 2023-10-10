#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:22:42 2023

@author: monika
"""

import math

def polysum(n, s):
    '''
        n = positive int, represents number of sides of polygon
        s = positive int, represents length of each side
        returns number rounded up to 4 decimals
    '''
    
    area = (0.25*n*(s**2))/math.tan(math.pi/n)
    perimeter = n*s
    print(area, perimeter)
    sm = area + perimeter**2
    return round(sm, 4)

