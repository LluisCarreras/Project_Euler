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
    
    idx = 37950
    succesives = 1
    latter_correct = False
    
    while True:
        divs_current = divisors(idx)
#        print(idx, "\t", divs_current)
        if len(divs_current) == num_of_consecs:
            divs_latter = divisors(idx - 1)         
            if len(divs_latter) == num_of_consecs:
                if are_distincts(divs_current, divs_latter):
                    succesives += 1
                    print(idx, "\t", divs_current, "\t", divs_latter, \
                              "\t", succesives)    
                    if succesives == num_of_consecs:
                        return idx - num_of_consecs + 1
                    latter_correct = True
                else:
                    latter_correct = False
                    succesives = 1
            else:
                latter_correct = False
                succesives = 1
        else:
            latter_correct = False
            succesives = 1
        idx += 1
                    
                        #print(num, "\t", distincts)
                
#                elif num != idx + num_of_consecs - 1 :
#                    still_correct = True
#                if num == idx + num_of_consecs - 1 and still_correct:
#                    result = list(range(idx, idx + num_of_consecs))
#                    return result
#                    continue_while = False
        

#primes = sieve(50000)
#print("Ya ta")
#print(primes[:15])
print(find_distincts(4))

#qty = 0
#for i in range(3, 10000):
#    if len(divisors(i)) == 4:
#        qty += 1
#    print(i, "\t", len(divisors(i)), "\t", qty)
  

