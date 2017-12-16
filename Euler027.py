# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:54:44 2016

@author: Lluís Carreras González

Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive 
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly 
divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 
primes for the consecutive values n = 0 to 79. The product of the 
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
"""


def is_prime(number):
    """
    Returns wether the given number is prime or not.
    """
    if number <= 0:
        return False
    elif number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True

def quadratic_primes(a, b):
    """
    Returns the n number of primes such that the consecutive numbers from 
    0 to n-1 applied to the formula n*n + a*n + b give primes, given a and b.
    """
    
    index = 0
    prime = True
    while prime:
        index += 1
        formula = index * index + a * index + b
        prime = is_prime(formula)
    return index
  
  
max_n = 0
max_a = None
max_b = None
for a in range(-999, 1000):
    for b in range(-999, 1000):
        if is_prime(b) and is_prime(1 + a + b):
            n = quadratic_primes(a, b)
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b
            print(a, "\t", b, "\t\tn: ", max_n, "\ta: ", max_a, "\tb: ", max_b)
            
result = max_a * max_b
print(result)            




#print(quadratic_primes(1, 41)) 
#print(quadratic_primes(-79, 1601)) 
#print(quadratic_primes(-999, 61))    