# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:27:34 2017

@author: Lluís

Square root digital expansion
Problem 80 

It is well known that if the square root of a natural number is not an integer, then it is 
irrational. The decimal expansion of such square roots is infinite without any repeating pattern 
at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one 
hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first 
one hundred decimal digits for all the irrational square roots.
"""


from decimal import getcontext, Decimal


getcontext().prec = 150


def total_digital_sum(num):
    sqr_num = (Decimal(num) ** Decimal(0.5))
    str_sqr_num = str(sqr_num)
    decimal_part = "".join(str_sqr_num.split('.'))
    print(decimal_part)
    digital_sum = sum([int(i) for i in decimal_part[:100]])
    return digital_sum
    
    
def is_irrational_square_root(num):
    sqr_num = (Decimal(num) ** Decimal(0.5))
    str_sqr_num = str(sqr_num)
    decimal_part = str_sqr_num.split('.')[1]
    if float(decimal_part) == 0.0:
        return False
    else:
        return True
        
total = 0        
for num in range(1, 101):
    if is_irrational_square_root(num):
        total += total_digital_sum(num)
    
print(total)
print(total_digital_sum(2))