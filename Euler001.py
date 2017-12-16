# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:52:00 2016

@author: Lluís


Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def multiples_of_3_and_5(limit):
    total = 0
    for i in range(limit):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    return total

print(multiples_of_3_and_5(1000))
