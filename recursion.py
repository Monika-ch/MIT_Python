#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 08:22:40 2023

@author: monika
"""

# TOWER OF HANOI (RECURSION)

def printMovew(fr, to):
    print("move from " + str(fr) + " to "  + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMovew(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
print(Towers(4, "P1", "P2", "P3" ))


# greatest common divisor of two positive integers
#1 iteration
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    div = a if a < b else b
    
    while div > 0:
        if a%div == 0 and b%div == 0:
            return div
        div -= 1

#2 recursion
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # base case: if b is zero, then a is the gcd
    if b == 0:
        return a
    # recursive case: call the function with b and a % b as the new parameters
    else:
        return gcdRecur(b, a % b)
"""
    For Example:
        
    Let’s say we call gcdRecur(9, 12). The function will check if b (12) is zero,
    and since it is not, it will return gcdRecur(12, 9 % 12). The % operator gives 
    the remainder of a division, so 9 % 12 is 9. 
    
    Now the function will run again with a = 12 and b = 9. It will check if 
    b (9) is zero, and since it is not, it will return gcdRecur(9, 12 % 9). 
    The remainder of 12 % 9 is 3. Now the function will run again with a = 9 and
    b = 3. It will check if b (3) is zero, and since it is not, it will return 
    gcdRecur(3, 9 % 3). The remainder of 9 % 3 is 0. 
    
    Now the function will run again with a = 3 and b = 0. It will check if b
    (0) is zero, and since it is, it will return a (3) as the answer. 
    This is the base case where the recursion stops.
    
    So, by using return gcdRecur(b, a % b), we are making the function call 
    itself repeatedly with smaller values of a and b, until we find the gcd. 
"""



def fib(x):
    """ assumes x is an int >= 0
        returns Fibonacci of x """
    if x==0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    


def isPalindrome(s):
    def toChar(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c>="a" and c<="z":
                ans += c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if char == len(aStr)//2:
        return True
    
    
    
    
def isIn2(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    if len(aStr) == 1 and char != aStr[0]:
        return False
    start = 0
    end = len(aStr)
    mid = (start+end)//2
    print(start, mid, end, aStr, aStr[mid])
    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn2(char, aStr[:mid])
    elif char > aStr[mid]:
        return isIn2(char, aStr[mid:])

    

    
    
    
    
    
    
    
    
    
    
    