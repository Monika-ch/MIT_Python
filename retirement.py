#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:09:30 2023

@author: monika
"""

import pylab as plt

# Example: Compound Interest and Graph Plotting

# computing compound interest
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly] 
    return base, savings
    
# displaying results vs month
def displayRetireMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label= 'retire:' + str(monthly))
        # print(xvals)
        # print(yvals)
        plt.legend(loc = 'upper left')
        plt.show()

displayRetireMonthlies([500,600,700,800,900,1000,1100], .05, 40*12)

# displaying results vs rate
def displayRetireRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, 
                 label= 'retire:'+ str(month)+':'+\
                         str(int(rate*100)))
        plt.legend(loc = 'upper left')
        plt.show()
displayRetireRates(800, [.03, .05, .07], 40*12)

# # displaying results vs both month and rate
# def displayRetireMonthsAndRates(monthlies, rates, terms):
#     plt.figure('retireMonthAndRate')
#     plt.clf()
#     plt.xlim(30*12, 40*12)
#     for monthly in monthlies:
#         for rate in rates:
#             xvals, yvals = retire(monthly, rate, terms)
#             plt.plot(xvals, yvals, 
#                      label= 'retire:'+ str(monthly)+':'+\
#                              str(int(rate*100)))
#             plt.legend(loc = 'upper left')
#             plt.show()
            
# displayRetireMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)

# displaying results vs both month and rate
# improvised displayRetireMonthsAndRates function from above
# with better data visualization display
def displayRetireMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireMonthAndRate')
    plt.clf()
    # set limit to x axis
    plt.xlim(30*12, 40*12)
    # create sets of labels
    monthLabels = ['k', 'b', 'y', 'r']
    rateLabels = ['--', '-', '^']
    for i in range(len(monthlies)):
        # pick new label for each month choice
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for i in range(len(rates)):
            # pick new label for each rate choice
            rate = rates[i]
            rateLabel = rateLabels[i%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, 
                     monthLabel+rateLabel, #create label for plot
                     label= 'retire:'+ str(monthly)+':'+\
                             str(int(rate*100)))
            plt.legend(loc = 'upper left')
            plt.show()
            
displayRetireMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)

