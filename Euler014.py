# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:01:38 2016

@author: Lluís Carreras González


Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)
 
def get_sequence(n):
    current_number = n
    sequence = [n]
    while current_number != 1:
        current_number = collatz(current_number) 
        sequence.append(current_number)
    return sequence

def get_longest_chain(n):
    max_length = 1
    max_number = 1
    for number in range(1, n): 
        sequence = get_sequence(number)
        sequence_length = len(sequence)
        if sequence_length > max_length:
            max_length = sequence_length
            max_number = number
        print(number, "\t", sequence_length, "\t", max_number)
    return sequence_length, max_number


print(get_sequence(13)) 
    
my_number = 1000000    
sequence_length, max_number = get_longest_chain(my_number)       
print("sequence_length: ", sequence_length) 
print("max_number:      ", max_number)  
        
      
        
        
        
        