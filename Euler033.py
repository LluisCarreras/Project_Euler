# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:14:28 2016

@author: Lluís Carreras González

Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less 
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""

from operator import mul
from fractions import Fraction
from functools import reduce


class Digit_Cancelling():
    """
    Class for problem 33 in Project Euler.
    """
    
    def __init__(self):
        """
        Create a new instance of the class Digit_Cancelling.
        """
        print(self.result())
    
    
    def is_dcf(self, num, den):
        """
        Checks wheter a faction is a digit cancelling fraction (dcf).
        num    is the numerator.
        den    is the denominator.
        """
        
        # Create string versions of num and den
        num_str = str(num)
        den_str = str(den)
        
        # If num or den are not two_digit numbers the fraction is not a dcf.
        if len(num_str) != 2 or len(den_str) != 2:
            return [False, 0]
        
        # Check wether there is a comon digit in num and den. If it exists,
        # checks wether num and den create a dcf faction.
        for n in num_str:
            if n in den_str:
                common_digit = n
                if common_digit == "0":
                    return [False, 0]
                original_fraction = Fraction(num, den)
                new_num = int(num_str.replace(common_digit, "", 1))
                new_den = int(den_str.replace(common_digit, "", 1))
                if new_num != 0 and new_den != 0:
                    new_fraction = Fraction(new_num, new_den)
                    if original_fraction == new_fraction:
                        return [True, int(common_digit)]
        
        # Otherwise, return False.    
        return [False, 0]
                
        
    def search_dcf(self):
        """
        Searches all the dcf's.
        """
        
        dcf_list = []
        # Iterate over all the feasible numerators and denominators.
        for n in range(10, 100):
            for d in range(n + 1, 100):
                new_dcf = (self.is_dcf(n, d))
                # Discard the trivial dcf's.
                if new_dcf[0] and new_dcf[1] != 0:
                    dcf_list.append(Fraction(n, d))
        print("\n", dcf_list)
        
        return dcf_list
        
        
    def result(self):
        """
        Gets the result of the class.
        """
        
        my_dcf_list = self.search_dcf()
        nums = [f.numerator for f in my_dcf_list]
        dens = [f.denominator for f in my_dcf_list]
        
        return Fraction(reduce(mul, nums, 1), reduce(mul, dens, 1))
        
        
if __name__ == '__main__':
    Digit_Cancelling()               
        
            
        
        
        
        
        