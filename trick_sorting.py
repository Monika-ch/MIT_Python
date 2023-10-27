#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:31:17 2023

@author: monika
"""
# Problem set trick question

def swapSort(L): 
    
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
# swapSort prints increasing order    
    
# If we make a small change to the line:
# for j in range(i+1, len(L)): such that the code becomes:
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
 # modSwapSort now orders the list in descending order for all lists.   
    
    
L = [4,2,3,1]    
swapSort(L)
print()
L = [4,2,3,1]  
modSwapSort(L)
    
    
    
    
    
    
    
    
    
    
    
    
    