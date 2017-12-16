# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:36:19 2016

@author: Lluís


Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

import math

def sum_of_squares(number):
    return int(sum([math.pow(i, 2) for i in range(1, number + 1)]))
    
def square_of_sum(number):
    return int(math.pow(sum([i for i in range(1, number + 1)]), 2))
    
def difference(number):
    return square_of_sum(number) - sum_of_squares(number)
    
print(sum_of_squares(10))
print(square_of_sum(10))
print(difference(10))

print(difference(100))
