#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:59:19 2023

@author: monika
"""


# Try/ except/ else/ finally

data = []

file_name = input("Provide a file name for data: ") # give input: "gradesData.py"

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()            
    
gradesData = []

# following code thorows error in special cases
'''
if data:
    for student in data:
        try:
            gradesData.append([student[0:2], [student[2]]])
        except IndexError:
            gradesData.append([student[0:2], []])
'''

# the above special case errors are handled in the code below
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])
            gradesData.append([name, [grades]])
        except ValueError:
            gradesData.append([student[:], []])
            
  
            
# RAISING AN EXCEPTION:

def get_ratios(l1, l2):
    ''' Assumes: l1 and l2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] '''

    ratios = []
    for index in range(len(l1)):
        try:
            ratios.append(l1[index]/float(l2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))    #NaN = Not a Number
        except:
            raise ValueError("get_ratios called with bad arg")
    return ratios
            

l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [5,6,7]
l4 = [5,6,7,0]



def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    # except ZeroDivisionError:          
    #     print("no grades data")       # print returns None
    except ZeroDivisionError:
        print("no grades data")
        return 0.0
        
test_grades = [[['peter', 'parker'],[10.0, 5.0, 85.0]],
               [['bruce', 'wayne'],[10.0, 8.0, 74.0]],
               [['captain', 'america'],[8.0, 10.0, 96.0]],
               [['deadpool'],[]]]

get_stats(test_grades)




# Assertion

def average(grades):
    assert not len(grades) == 0, "no grades data"
    return sum(grades)/len(grades)
    ''' raises an AssertionError if it is given an empty list for grades
        otherwise runs ok '''

    