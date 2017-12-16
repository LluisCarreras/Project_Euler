# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:06:05 2016

@author: Lluís Carreras González

Module Euler_Project.py

This module contains the functions created to solve Euler Project problems 
that can be useful in other problems.
"""

import math


def is_prime(num):
    """
    Return True if the given number num is prime.
    """
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True
    
    
def factorial(num):
    """
    Return the factorial of the given number num.
    
    Taken from Problem 20.
    """
    
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

    

def sieve(num):
    """
    Return a list of the primes up to the given number num, using the Sieve
    of Erathostenes.
    """
    
    my_primes = [i for i in range(0, num)]
    my_primes[1] = 0
    for number in range(2, int(math.sqrt(num)) + 1, 1):
        for prime in range(number * 2, num, number):
            if my_primes[prime] != 0:
                my_primes[prime] = 0
    return [prime for prime in my_primes if prime != 0]
    
    
def divisors(num):
    """
    Return a list with the divisors of the given number.
    """
    divs = set()
    for i in range(2, num):
        if is_prime(i):
            while num % i == 0:
                divs.add(i)
                num /= i
    return divs
    
    
def next_prime(num):
    """
    Return the next prime following the given number.
    """
    
    test_num = num + 1
    while not is_prime(test_num):
        test_num += 1
    
    return test_num
    
    
def permutations(digits, my_list):
    """
    Returns the list of permutations that can be made from the objects in
    the given list.
    """
    
    if len(my_list) > 0 and len(my_list[0]) == len(digits):
        return my_list
    else:
        new_list = []
        for item in my_list:
            for digit in digits:
                if digit not in item:
                    new_item = item + digit
                    new_list.append(new_item)
                    
        return permutations(digits, new_list)
        
