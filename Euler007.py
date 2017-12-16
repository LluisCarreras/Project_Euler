# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:45:37 2016

@author: Lluís Carreras González

10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(number):
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True

def calculate_nth_prime(n):
    nth_prime = 1
    primes_found = 0
    index = 1
    while primes_found <= n:
        if index == 1 or index == 2 or is_prime(index):
            primes_found += 1
            nth_prime = index
        index += 1
    return nth_prime
    
print(calculate_nth_prime(6))     

print(calculate_nth_prime(10001))
                
    