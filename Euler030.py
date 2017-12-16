# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:18:35 2016

@author: Lluís Carreras González

Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum 
of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.

"""

import math


class Digit_powers():
    """
    Class for problem 30 in Project Euler.
    """
    
    def __init__(self, rang, pwr):
        """
        Create a new Digit_Powers instance.
        
        rang:   The range of numbers to test in order to find the numbers
                that can be written as the sum of the pwr-th powers of their 
                digits.
        pwr:    The power of the digits.
        """        
        self._rang = rang
        self._pwr = pwr
        
    def is_pwr_num(self, n):
        """
        Check wether the n number can be written as the sum of the fifth 
        powers of their digits.
        
        Return True if so and False otherwise.
        """        
        return sum([math.pow(int(i), self._pwr) for i in str(n)]) == n
       
    def pwr_nums(self):
        """
        Return a list with the numbers that can be written as the sum of 
        the n-th powers of their digits.
        """
        return [i for i in range(2, self._rang + 1) if self.is_pwr_num(i)]   
        
    def sum_pwr_nums(self):
        """
        Return the sum of the numbers that can be written as the sum of 
        the n-th powers of their digits.
        """        
        return sum(self.pwr_nums())
   
   
if __name__ =='__main__':
    """
    Test the class for pwr = 4 and pwr = 5.
    """  
    for pwr in (4, 5):
        dig_pwrs = Digit_powers(1000000, pwr)
        pwr_nums = dig_pwrs.pwr_nums()
        the_sum = dig_pwrs.sum_pwr_nums()
        
        print(pwr, "th power numbers: ")
        for n in pwr_nums:
            print("\t", n)
            
        print("\nSum:\t", the_sum, "\n\n")
     

