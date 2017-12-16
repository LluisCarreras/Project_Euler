# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:09:50 2016

@author: Lluís Carreras González

Odd period square roots
Problem 64

All square roots are periodic when written as continued fractions and can 
be written in the form:

.....


It can be seen that the sequence is repeating. For conciseness, we use the 
notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats 
indefinitely.

The first ten continued fraction representations of (irrational) square 
roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""

import math
import time


def first_term(num):
    """
    Return the coeficients of the first term.
    """
    
    i = int(math.sqrt(num))
    d2 = i
    
    return i, d2


def next_term(n, d1, d2):
    """
    Return coeficientss of the next terms after the first one.
    
    Parameters:
    n = numerator
    d1 = number under the square root in the denominator 
    d2 = independent term in the denominator
    
    in the formula: n / (sqr(d1) - d2))
    
    Return:
    i = integer, independent term
    num = numerator
    den1 = number under the square root in the denominator 
    den2 = independent term in the denominator
    
    
    in the formula: i + num / (sqr(d1) - den2) 
    """
    
    new_num = math.sqrt(d1) + d2  
    num = int((d1 - d2 ** 2) / n)
    i = int(new_num // num)
    den2 = int(d2 - i * num)
    den1 = d1
    
    return i, num, den1, den2
  

def find_digits(num):
    """
    Return the independent integer term and the sequence of tems that are
    repeated in the succesive fractions.
    """
    
    first = first_term(num)
    indep = first[0]
    digits_in_den = []
    n, d1, d2 = 1, num, first[1]
    
    while True:
         next_t = next_term(n, d1, d2) 
         n, d1, d2 = next_t[1], num, - next_t[3]
         digits_in_den.append(list(next_t))
         
         if len(digits_in_den) > 1:
             if digits_in_den[-1] == digits_in_den[0]:
                 my_indeps = [ind[0] for ind in digits_in_den]
                 return indep, my_indeps[:-1]

         
time_ini = time.time()
        
count = 0    
for n in range(2, 10001):
    if math.sqrt(n) - int(math.sqrt(n)) != 0:
        if len(find_digits(n)[1]) % 2 == 1:
            count += 1
print("Result: \t\t", count, "fractions for N ≤ 10000 have an odd period")

time_end = time.time()
time_total = time_end - time_ini
print("Time required: \t", "{0:.4f}".format(time_total), "seconds") 
    
