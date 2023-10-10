#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:46:27 2023

@author: monika
"""



# Exercise
low = 0
high = 100
guess= int((low+high)/2)
inputStr = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(guess) + "?")
keyedInput = input(inputStr)

while (low < high):
    if keyedInput == "h":
        high = guess
    elif keyedInput == "l":
        low = guess
    elif keyedInput == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
    guess= int((low+high)/2)
    print("Is your secret number " + str(guess) +"?")
    keyedInput = input(inputStr)
print("Game over. Your secret number was:", guess)


#Cube
cube = 27
guess = 0.0
epsilon = 0.01
increment = 1.5
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    print(abs(guess**3 - cube))
    guess += increment
    num_guesses += 1
    print("guessed number is:", guess)
print("num of guesses =", num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)
    
    
    
    
# Binary Search or Bisection Search
# a) for square root
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high+low)/2.0

while abs(ans**2 -x) >= epsilon:
    print("low=", str(low), "high=", str(high), "ans=", ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print("numGuesses=", numGuesses)
print(ans, "is close to square root of", x)

# b) for cube root
cube=54
epsilon = 0.01
numGuesses = 0
low = 0
high = cube
ans = (high+low)/2.0

while abs(ans**3 - cube) >= epsilon:
    print("low=", str(low), "high=", str(high), "ans=", ans)
    numGuesses += 1
    if ans**3 < cube:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print("numGuesses=", numGuesses)
print(ans, "is close to cube root of", cube)