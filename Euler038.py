# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:33:00 2016

@author: Lluís Carreras González

Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
and 5, giving the pandigital, 918273645, which is the concatenated product 
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(s):
    """
    Evaluate wether the given string of digits s is pandigital.
    """
    # Create a list and a set with the string of digits. Only if their
    # lengths are equal it means that the digits are different.
    # Only digits contained in the sequence "123456789" are allowed.
    if  len(set(s)) == len(list(s)):
        for dig in s:
            if dig not in "123456789":
                return False
        return True
    else:
        return False
 
       
pandigital_nums = []
for n in range(1, 10000000):
    concatenation = ""
    idx = 1
    while len(concatenation) < 9:
        concatenation += str(idx * n)
        idx += 1
    if len(concatenation) == 9:
        if is_pandigital(concatenation):
            pandigital_nums.append(int(concatenation))
            print(n, "\t", idx - 1, "\t", concatenation)
            
print(pandigital_nums)
print(max(pandigital_nums))            