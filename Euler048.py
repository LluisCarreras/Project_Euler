# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:13:37 2016

@author: Lluís Carreras González

Self powers
Problem 48

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

import math


def pseudo_pow(num):
    """
    Pseudo power function that returns the result of multiplying the given 
    number num by the last ten digits of the former multiplication.
    """
    
    pseudo = num
    divisor = math.pow(10, 10)
    for i in range(num - 1):
        pseudo = int((pseudo * num) % divisor)
    return pseudo

    
result = 0    
for num in range(1, 1001):
    result += pseudo_pow(num)

print(str(result)[-10:])