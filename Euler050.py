# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:37:16 2016

@author: Lluís Carreras González

Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a 
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""


import Euler_Project as ep


# Maximum number considered.
max_num = 1000000

# List of primes up to the maximum number.
primes = ep.sieve(max_num)

# Maximum number of consecutive primes found.
max_consec = 0

# best     The best results obtained.
# best[0]  Prime obtained from the longest sum of consecutive primes.
# best[1]  Number of consecutive primes.
# best[2]  Index of the first among the consecutive primes.
best = 0, 0, 0 

# Index of the prime inside of the list primes.
prime_idx = 0


for idx in range(len(primes)):
    # Iterate in the list of primes. For every prime, search the maximum 
    # sequence of consecutive primes whose sum is a prime in the list. Stop 
    # the iteration if finding a longest sequence is not feasible.

    partial_sum = 0 
    max_consec = 0
    prime_idx = idx
    
    if sum(primes[idx : idx + best[1]]) > max_num:
        # Stop the iteration if finding a longest sequence is not feasible.
        break
    
    while partial_sum < max_num and prime_idx < len(primes) - 1:       
        if ep.is_prime(partial_sum):           
            if max_consec > best[1]:
                best = partial_sum, max_consec, idx
        max_consec += 1
        prime_idx += 1
        partial_sum += primes[prime_idx]

    print(idx, "\t", best)

            
print(best)       
    
