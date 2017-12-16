# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:05:19 2016

@author: Lluís Carreras González

Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all 
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital 
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


import math


def is_pandigital(s, expr):
    """
    Evaluate wether the given string of digits s is pandigital.
    """
    # Create a list and a set with the string of digits. Only if their
    # lengths are equal it means that the digits are different.
    # Only digits contained in the sequence "123456789" are allowed.
    if  len(set(s)) == len(list(s)):
        for dig in s:
            if dig not in expr:
                return False
        return True
    else:
        return False
        
def model(n):
    """
    Return the model string for n.
    """
    
    return "".join([str(i) for i in range(1, n + 1)])
    
    
def max_pandigital(n):
    """
    Return the maximum number that can be made from the digits from 1 to the 
    given n.
    """
    
    return int("".join([str(i) for i in range(n, 0, -1)]))
    

def is_prime(num):
    """
    Evaluate wether the given number num is prime.
    """
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True
 
    
def get_solution():
    """
    Return the maximum pandigital prime.
    """
    
    for n in range(9, 0, -1):
        print(n)
        test_num = max_pandigital(n)
        the_model = model(n)
        min_num = int(the_model)
        while test_num >= min_num:
            if  is_pandigital(str(test_num), the_model):
                if is_prime(test_num):
                    return test_num
            test_num -= 1
    return -1
   
print(get_solution())
    