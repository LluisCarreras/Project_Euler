# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:14:35 2016

@author: Lluís Carreras González

Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?
"""


import math
import time


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
    
    
def are_distincts(divs_1, divs_2):
    for div1 in divs_1:
        if div1 in divs_2:
            return False
    return True
 
 
def find_distincts(num_of_consecs):
    
#    idx = 59000
    idx = 79000
#    idx = 4
    my_dict = {}
    
    time_1 = time.time()
       
    while True:
        succesives = 0
        for num in range(idx, idx + num_of_consecs):
            if idx % 1000 == 0:
                time_2 = time.time()
                print(idx, "\t", time_2 - time_1)
                time_1 = time_2
            if num not in my_dict:
                my_dict[num] = divisors(num) 
            if len(my_dict[num]) != num_of_consecs:
                idx += 1
                break
            else:
                succesives += 1 
            
        if succesives == num_of_consecs:
            print([v for k, v  in my_dict.items() 
                    if k in range(idx, idx + num_of_consecs)])
            for num in range(idx + 1, idx + num_of_consecs):
                if not are_distincts(my_dict[num], my_dict[num - 1]):
                    break
                return idx

print(find_distincts(4))

