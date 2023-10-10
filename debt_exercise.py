#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:45:52 2023

@author: monika
"""

def payingDebt(balance, annualInterestRate, monthlyPaymentRate):
    '''

    Parameters
    ----------
    balance : number
    annualInterestRate : float
    monthlyPaymentRate : float

    Returns
    -------
    float rounded upto 2 decimals

    '''
    rem_bal = balance
    month_int = annualInterestRate/12
    for i in range(12):
        min_pay = monthlyPaymentRate * rem_bal
        rem_bal = rem_bal - min_pay
        interest = month_int * rem_bal 
        rem_bal = rem_bal + interest
    print("Remaining balance:", round(rem_bal, 2))
    
    
def minimumFixedPayment(balance, annualInterestRate):
    month_int = annualInterestRate/12
    min_pay = balance/12
    rem_bal = balance
    count = 0
    
    if min_pay%10 != 0:
        remainder = min_pay%10
        min_pay += 10 - remainder
        
    while rem_bal > 0:
        count += 1
        for i in range(12):
            rem_bal -= min_pay
            interest = rem_bal * month_int
            rem_bal += interest
        print(rem_bal)
        if rem_bal > 0:
            min_pay += 10
            rem_bal = balance
        else:
            print(count)
            break
    print("Lowest Payment:", int(min_pay))
    
    
def minimFixedPayment(balance, annualInterestRate):
    month_int = annualInterestRate/12
    max_bal_with_interest = (balance * annualInterestRate) + balance
    min_pay = balance/12
    max_pay = max_bal_with_interest/12
    rem_bal = balance
    count = 0
        
    mid = (min_pay + max_pay)//2
    print("min_pay", min_pay, "max_pay:", max_pay)
    print("mid:", mid)  
     
    while rem_bal > 0:
        count += 1
        for i in range(12):
            rem_bal = rem_bal - min_pay
            interest = rem_bal * month_int
            rem_bal = rem_bal + interest
        print(rem_bal)
        if rem_bal > 0:
            min_pay += 10
            rem_bal = balance
        else:
            print(count)
            break
       
    print("max_bal_with_interest:", max_bal_with_interest)
    print("min_pay", min_pay)
    print("max_pay:", max_pay)
    print("Lowest Payment:", int(min_pay))
    
def minFixedPayment(balance, annualInterestRate):   
    
    count = 0

    # Calculate the monthly interest rate
    monthlyInterestRate = annualInterestRate / 12.0

    # Calculate the lower bound of the monthly payment
    lowerBound = balance / 12

    # Calculate the upper bound of the monthly payment
    upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

    # Initialize a variable to store the guess for the monthly payment
    monthlyPayment = (lowerBound + upperBound) / 2

    # Initialize a variable to store the remaining balance after one year
    remainingBalance = balance
    while abs(remainingBalance) > 0.01:
        count += 1
        # Reset the remaining balance to the original balance
        remainingBalance = balance
        # Loop through 12 months and update the remaining balance after each payment
        for month in range(12):
            # Subtract the monthly payment from the remaining balance
            remainingBalance -= monthlyPayment
            # Add the monthly interest to the remaining balance
            remainingBalance += monthlyInterestRate * remainingBalance
        # If the remaining balance is positive, increase the lower bound of the monthly payment
        if remainingBalance > 0:
            lowerBound = monthlyPayment
        # If the remaining balance is negative, decrease the upper bound of the monthly payment
        elif remainingBalance < 0:
            upperBound = monthlyPayment
        # Update the guess for the monthly payment by taking the average of the lower and upper bounds
        monthlyPayment = (lowerBound + upperBound) / 2
        
    print(count)
    # Print the lowest monthly payment rounded to two decimal places if it was found within 30 seconds
    if abs(remainingBalance) <= 0.01:
        print("Lowest Payment: " + str(round(monthlyPayment, 2)))

