# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:09:12 2016

@author: Lluís Carreras González

Prime pair sets
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two 
primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of 
these four primes, 792, represents the lowest sum for a set of four primes 
with this property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
"""


import Euler_Project as ep


def evaluate(my_candidates):
    for prime1 in my_candidates:
        for prime2 in my_candidates:
            if prime1 != prime2:
                print(my_candidates)
                if not ep.is_prime(int(str(prime1) + str(prime2))) \
                        or not ep.is_prime(int(str(prime2) + str(prime1))):
                    return False
    return True 
             



def prime_pair_sets():
    my_primes = ep.sieve(3000000)
    for p1 in [3]:
        for p2 in [7]:
            for p3 in [109]:
                for p4 in [673]:
                    for p5 in my_primes:
                        candidates = [p1, p2, p3, p4, p5]
                        if len(set(candidates)) == len(candidates):
    #                    print(candidates)
                            if evaluate(candidates):
                                return candidates


print() 
result = prime_pair_sets()                          
print(result)
print(sum(result))
               
                                    
                   
            
                    
 