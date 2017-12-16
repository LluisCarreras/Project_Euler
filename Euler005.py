# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:59:40 2016

@author: Lluís


Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
"""

import math

def is_prime(number):
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                #print(number, "    ", i)
                return False
    #print(number)
    return True       
     
def list_of_primes(number):
    result = []
    for i in range(2, number + 1):
        if is_prime(i):
            result.append(i)
            #print(result)
    return result
    
def dict_of_primes(my_list):
    return {i:1 for i in my_list}
    
def decomposition(number):
    my_dict = {}
    for i in range(2, number + 1):
        while number % i == 0:
            number /= i
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
            
    return my_dict
    
limit = 20
my_dict_of_primes = dict_of_primes(list_of_primes(limit))
#print(my_dict_of_primes)

for i in range(2, limit + 1):
    my_primes = decomposition(i)
    #print(i, "\t", my_primes)
    for prime, exponent in my_primes.items():
        if exponent > my_dict_of_primes[prime]:
            my_dict_of_primes[prime] = exponent
print(my_dict_of_primes)
            
smallest_multiple = 1
for prime, exponent in my_dict_of_primes.items():
    smallest_multiple *= int(math.pow(prime, exponent))
    
print(smallest_multiple)
