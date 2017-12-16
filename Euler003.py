# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:17:07 2016

@author: Lluís


Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def largest_prime_factor(number):
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number /= i
    print(factors)
    return max(factors)

print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
