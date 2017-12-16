# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:18:29 2016

@author: Lluís Carreras González

Powerful digit sum
Problem 56

A googol (10**100) is a massive number: one followed by one-hundred zeros; 
100**100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the 
maximum digital sum?
"""

import math


def digital_sum(a, b):
    """
    Return the digital sum of a**b.
    """
    
    return sum([int(i) for i in str(int(math.pow(a, b)))])
   

def maximum_digital_sum():   
    maximum = 0    
    for a in range(100):
        for b in range(100):
            my_digital_sum = digital_sum(a, b)
            if my_digital_sum > maximum:
                maximum = my_digital_sum
                max_a = a
                max_b = b
                max_pwr = math.pow(a, b)
    return max_a, max_b, max_pwr, maximum

            
print(maximum_digital_sum())
print(digital_sum(88,98))
 

# TODO: Repassar a vam que passa, dona fall però sembla que tot estigui bé   