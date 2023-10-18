#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:23:43 2023

@author: monika
"""

"""
Write a generator, genPrimes, that returns the sequence of prime numbers on
 uccessive calls to its next() method: 2, 3, 5, 7, 11, ...
Have the generator keep a list of the primes it's generated. 
A candidate number x is prime if (x % p) != 0 for all earlier primes p."""


def genPrimes():
    primes = []
    n = 2
    while True:
        isNPrime = True
        if len(primes) == 0:
            primes.append(n)
            yield n
            n += 1
        else:
            for p in primes:
                if n % p == 0:
                    isNPrime = False
                    n += 1
                    break
            if isNPrime == True:
                primes.append(n)      
                yield n
      
primeNums = genPrimes()
print(primeNums.__next__())
print(primeNums.__next__())
print(primeNums.__next__())
print(primeNums.__next__())
print(primeNums.__next__())
print(primeNums.__next__())
print(primeNums.__next__())
print(primeNums.__next__())
print(primeNums.__next__())
