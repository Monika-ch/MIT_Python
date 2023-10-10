#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 23:11:11 2023

@author: monika
"""
string = "shcuw683hello worldcgs"
myStr = "hello world"

if myStr == "hi there":
    print("hi there")
elif myStr == "who's there":
    print("who's there")
elif myStr in string:
    print("hello world")
else:
    print("HELLO THERE!")
    
    
''' Cube Root Example (only works on positive numbers)'''
x = int(input("Enter a number1: "))

ans = 0
while ans**3 < x:
    ans += 1
if ans**3 != x:
    print(str(x) + " is not a perfect cube!")   
else:
    print("Cube root of " + str(x) + " is " + str(ans) + "!")
    
    
# Cube Root Example (covers edge cases and works on negative numbers too)
x = int(input("Enter a number2: "))

ans = 0
while ans**3 < abs(x):
    ans += 1
if ans**3 != abs(x):
    print(str(x) + " is not a perfect cube!")   
else:
    if x < 0:
        ans = -ans
    print("Cube root of " + str(x) + " is " + str(ans) + "!")
    
    
# Cube Root and FOR Loop:
cube = int(input("Enter a number3: "))

for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube,"isn't a perfect cube")
else:
    if cube < 0:
        guess = -guess
        print("Cube root of", cube,"is", guess)
        
        

