#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:19:49 2023

@author: monika
"""

# LISTS

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2  #concats both lists L1 and L2

L1.append(8) #adds 8 to end of list L1; now L1 = [1,2,3,8]
L1.extend([7,9]) #concats/extends L1; now L1 = [1,2,3,8,7,9]
del(L1[3]) # deletes 8 from list which is at index 3; L1 = [1,2,3,7,9]
L1.pop() # pops out last elem 9 from List and returns it; L1 = [1,2,3,7]
L1.remove(7) # looks up 7 and removes it if present; L1 = [1,2,3]
L1.remove(17) # looks up 17, didnt find so throws error; L1 = [1,2,3]
L1.append(3) # L1 = [1,2,3,3]
L1.remove(3) # only removes 1st instance of 3; L1 = [1,2,3]
L1.insert(0, 100) # mutates L1; inserts 0, 100 in the beginning ; L1 = [0,100,1,2,3]
L1.pop(1) # removes 100 from index 1; L1 = [0,1,2,3]
L1.count(40) # returns 0 because 40 is not present in L1


# Converting STRING to LIST

s = "abc"
list(s) # => outputs ['a','b','c']
s.split() # => ["abc"]

s = 'i am a string'
s.split() # => ["i", "am", "a", "string"]

s="I <3 cs"
list(s) # => returns ['I', ' ', '<', '3', ' ', 'c', 's']
s.split("<") # => returns ['I ', '3 cs']

L = ['a', 'b', 'c']
"".join(L) # => returns "abc"
"_".join(L) # => returns 'a_b_c'



# Sorting and reversing a list

L = [8,6,0,3]

sorted(L) # => outputs [0, 3, 6, 8]; does NOT MUTATE L
L.sort() # => mutates L to [0,3,6,8]
L.reverse() # => mutates L to [8, 6, 3, 0]
L.index(8) # => returns only 1st index since 8 is present at 0 index, returns 0
L.index(80) # => throws error coz 80 is not in L



# RANGE in FOR loop

range(5) # equivalent to tuple [0,1,2,3,4]
range(2,6) # equivalent to tuple [2,3,4,5]
range(5, 2, -1) # equivalent to tuple [5,4,3]
