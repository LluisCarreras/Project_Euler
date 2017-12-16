# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 23:36:22 2016

@author: Lluís Carreras González


Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(num):
    """
    Return the factorial of the given number num.
    """
    
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
 
 
number = 100       
result = sum([int(f) for f in str(factorial(number))])
print(result)