# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:30:21 2016

@author: Lluís Carreras González

Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six 
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 
5-digit number is the first example having seven primes among the ten 
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 
56773, and 56993. Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight prime 
value family.
"""


import Euler_Project as ep


def next_prime(num):
    """
    Return the next prime following the given number.
    """
    
    test_num = num + 1
    while not ep.is_prime(test_num):
        test_num += 1
    
    return test_num
  
  
def repeated_digit(num, dig):
    """
    Returns True if the given number has two or more digits dig.
    """

    digit_idxs = []
    for idx in range(len(str(num))):
        if str(num)[idx] == str(dig):
            digit_idxs.append(idx)
            
    if len(digit_idxs) > 1:
        return True
    else:
        return None


def digit_location(num, dig):
    """
    Returns a list with the location of the "0" digits in the given number.
    """
    
    my_str_list = list(str(num))
    
    return [i for i in range(len(my_str_list)) if my_str_list[i] == str(dig)]

        
def prime_digits(num_primes):  
    """
    Solve the problem stated in problem 51.
    """
    
    #Initialitation of the iteration.
    test_num = 10000   
    num_primes_temp = 0
    
    # Iterate while the number of primes is less that the required value.
    while num_primes_temp < num_primes: 
        # Get the next prime.
        test_num = ep.next_prime(test_num)
        # For every feasible digit, in the range 0-9, iterate in order to
        # transform the prime number replacing any repetition of a digit by
        # every digit in the range 0-9.
        for digit in "0123456789":
            num_fails = 0
            num_primes_temp = 0
            # Consider only the primes with any repeated digit.
            if repeated_digit(test_num, int(digit)):
                locations = digit_location(test_num, digit)
                for dig in "0123456789":
                    test_str = list(str(test_num))
                    # Make the replacement.
                    for value in locations:
                        test_str[int(value)] = str(dig)
                    new_test = int("".join(test_str))
                    # If the prime with the repeated digit replaced is also a
                    # prime, increment the number of primes found.
                    if ep.is_prime(new_test) and \
                            len(str(new_test)) == len(str(test_num)):
                        num_primes_temp += 1
                    #If the prime with the repeated digit replaced is not a
                    # prime, increment the number of fails in order the break 
                    # the iteration and discard the original primes that can't
                    # achieve the objective of finding a gigen number of 
                    # primes obtained through replacements.
                    else:
                        num_fails += 1
#                    print(digit, "\t", dig, "\t", test_num, "\t", new_test, \
#                            "\t", locations, "\t", num_primes_temp)
                    if num_fails > 10 - num_primes:
                        break
                    # Return the initial prime with no replacements from
                    # which the required number of primes is achieved.
                    if num_primes_temp == num_primes:
                        return test_num
    

print(prime_digits(8))        
        
        