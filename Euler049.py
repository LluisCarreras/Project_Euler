# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:57:19 2016

@author: Lluís  Carreras González

Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
"""

import math


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


def permutations(digits, my_list):
    """
    Return the list of permutations that can be made from the objects in
    the given list.
    """
    
    if len(my_list) > 0 and len(my_list[0]) == 2 * len(digits):
        return my_list
    else:
        new_list = []
        for item in my_list:
            for digit in digits:
                if digit not in item:
                    new_item = item + digit
                    new_list.append(new_item)
        return permutations(digits, new_list)


def sequences(num):
    my_list = [x + y for x, y in list(zip(list(str(num)), list("abcd")))]
#    print(my_list)
    
    permut = list(set([i[0] + i[2] + i[4] + i[6] 
            for i in permutations(my_list, my_list)]))
#    print(permut)
    
    permut = sorted([int(i) for i in permut if is_prime(int(i))])
#    print(permut)
    
    my_dict = {permut[i]:set() for i in range(len(permut))}
#    print(my_dict)
    
    for idx1 in range(1, len(permut)):
        for idx2 in range(idx1):
            my_dict[permut[idx1]].add(permut[idx1] - permut[idx2])   
            my_dict[permut[idx2]].add(permut[idx1] - permut[idx2]) 
#    print(my_dict)
    
    new_dict = {}
    for k, v in my_dict.items():
        for n in v:
            if n in new_dict:
                new_dict[n].append(k)
            else:
                new_dict[n] = [k]
#    print(new_dict)
    
    return {k:v for k, v in new_dict.items() if len(v) >= 3}

    
#print(my_dict)
result_set = set()
for num in range(1000, 10000):
    if '0' not in list(str(num)):
        seq = sequences(num) 
        for k, v in seq.items():
            if k == 3330:
                result_set.add(''.join(([str(i) for i in v])))
    
print(result_set)    
