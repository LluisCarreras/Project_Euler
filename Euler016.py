# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 21:43:03 2016
@author: Lluís Carreras González

Power digit sum
Problem 16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

import math


number = int(math.pow(2, 1000))
number_str = str(number)
    
print(number_str)
    
outcome = sum([int(c) for c in number_str])
print(outcome)
