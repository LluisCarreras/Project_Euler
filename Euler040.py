# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:44:01 2016

@author: Lluís Carreras González

Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of 
the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


from math import pow
from operator import mul
from functools import reduce


# Create the decimal fraction up to its millionth digit.
dec_fraction = ""
idx= 1
while len(dec_fraction) <= 1000001:
    dec_fraction += str(idx)
    idx += 1

# Get the digits "d" of the expression.
digits = [int(dec_fraction[i - 1]) 
        for i in [int(pow(10, p)) for p in range(7)]]
            
# Get the final expression
expression = reduce(mul, digits, 1)

# Print the results.
print("Digits:     ", digits)
print("Expression: ", expression)