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
    

def sieve(n):
    my_primes = [i for i in range(0, n + 1)]
    my_primes[1] = 0
    print(int(math.sqrt(n)) + 2)
    for number in range(2, int(math.sqrt(n)) + 1, 1):
        if number % 1000 == 0:
            print(number)
        for prime in range(number * 2, n, number):
            if my_primes[prime] != 0:
                my_primes[prime] = 0
        #print(number, "\t", list(range(number * 2, n, number)))
        #print(number, "\t", my_primes)
                
    return [p for p in my_primes if p != 0]
 
    
def get_solution():
    """
    Return the maximum pandigital prime.
    """
    
    primes = reversed(sieve(max_pandigital(9)))
    for n in range(8, 0, -1):
        the_model = model(n)
        n_primes = [p for p in primes if (len(p) == n)]
        for prime in n_primes:
            if is_pandigital(str(prime), the_model):
                print(n, "\t", prime)
                return prime
    return -1
   
print(get_solution())
    