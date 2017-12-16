# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 23:47:28 2016

@author: Lluís Carreras González

Diophantine equation
Problem 66
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 649**2 – 13×180**2 = 1.

It can be assumed that there are no solutions in positive integers when D 
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the 
following:

3**2 – 2×2**2 = 1
2**2 – 3×1**2 = 1
9**2 – 5×4**2 = 1
5**2 – 6×2**2 = 1
8**2 – 7×3**2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is 
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest 
value of x is obtained.
"""

from fractions import Fraction
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
                 
                 
def convergent(n, values):
    """
    Function that returns the convergent terms up to the n-th term.
    
    Parameters:
    n      = The order of the maximum term that will be returned.
    values = A list with the first n terms of the sequence of partial values.
    """
    
    nums = [0, 1]
    dens = [1, 0]
    values.insert(0, 0)
    values.insert(0, 0)
    for idx in range(2, n + 2):
        new_num = values[idx] * nums[idx - 1] + nums[idx - 2]
        new_den = values[idx] * dens[idx - 1] + dens[idx - 2]
        nums.append(new_num)
        dens.append(new_den)
    nums.remove(0)
    nums.remove(1)
    dens.remove(1)
    dens.remove(0)
    return list(map((lambda x, y : Fraction(x, y)), nums, dens))

    
def term(num):
    """
    Returns the term from the succesive convergents that gives the values of
    the x and the y.
    """
    
    test = find_digits(num)
    indep = test[0]
    the_list = test[1] * 3
    the_list.insert(0, indep)
    if len(test[1]) % 2 == 1:
        idx = 2 * len(test[1])
    else:
        idx = len(test[1]) 
    return convergent(idx, the_list[:idx])[-1]


time_ini = time.time() 

D_max = 0
x_max = 0
squares = [int(i ** 2) for i in range(2, 32)]
D_list = [i for i in range(2, 1001) if i not in squares]

# According to Wikipedia:
# https://en.wikipedia.org/wiki/Continued_fraction
for D in D_list:
    frac = term(D)
    x = frac.numerator
    y = frac.denominator
    if x > x_max:
        x_max = x
        D_max = D
        
print("Value of D ≤ 1000 for which the largest value of x is obtained: ", \
        D_max)

time_end = time.time()
time_total = time_end - time_ini
print("Time required: \t", "{0:.4f}".format(time_total), "seconds")     