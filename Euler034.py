# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:20:09 2016

@author: Lluís Carreras González

Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def factorial(num):
    """
    Calculate the factorial of the given number.
    """
    
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
 

def sum_of_factorials(n):
    """
    Calculate the sum of the factorials of the digits of the given number.
    """
    
    return sum([factorial(int(digit)) for digit in str(n)])
        
    
result = sum([n for n in range(3, 100000) if n == sum_of_factorials(n)])
print(result)        