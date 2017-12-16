# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:22:21 2016

@author: Lluís Carreras González

Convergents of e
Problem 65

The square root of 2 can be written as an infinite continued fraction.

.....

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates 
that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for 
square roots provide the best rational approximations. Let us consider the 
convergents for √2.

.......
 
Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the 
continued fraction for e.
"""


from fractions import Fraction
import time


def convergent(n, values):
    """
    Recursive function that returns the n-th convergent term.
    
    Parameters:
    n      = The order of the term that will be returned.
    values = A list with the first n terms of the sequence of partial values.
    """
    
    if not values:
        return 0
    elif len(values) == n:
        return 2 + convergent(n, values[1:])
    else:
        return Fraction(1, values[0] + convergent(n, values[1:]))
        
        
time_ini = time.time()       
        
partial_values = [n for m in [(1, 2 * i, 1) for i in range(1, 40)] for n in m]
partial_values.insert(0, 2)
#print(terms)

n = 100
nth_convergent = convergent(n, partial_values[:n])
print("n = ", n, "\t Convergent = ", nth_convergent)
print("Numerator = ", nth_convergent.numerator)

the_sum = sum([int(dig) for dig in str(nth_convergent.numerator)])
print("Sum of digits in the numerator = ", the_sum)

time_end = time.time()
time_total = time_end - time_ini
print("Time required: \t", "{0:.4f}".format(time_total), "seconds") 