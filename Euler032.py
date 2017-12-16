# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:27:17 2016

@author: Lluís Carreras González

Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
"""


import math

class Pandigital_Products():
    """
    Class for problem 32 in Project Euler.
    """
    def __init__(self, n):
        """
        Create a new instance of the class Pandigital_Products
        """
        # n is the range of the sequence
        self.n = n
        # seq is the maximum feasible number that can be a pandigital product.
        self.seq = self.create_sequence(self.n)
        
        # Create a list of pandigital products, where every item is a list 
        # that contains the multiplicand, the multiplier and the product.
        diff_idents = self.find_pandigitals(self.seq)  
        
        # Create a list with the pandigital products.          
        prods = [i[2] for i in diff_idents] 
        
        # Obtain the sum of all the pandigital products.
        sum_prods = sum(prods)        
        
        # Print the results                  
        print(len(diff_idents))
        print(diff_idents)
        print(prods)       
        print(sum_prods)


    def has_diff_digits(self, s):
        """
        Evaluates wether the given string of digits s is made of different
        allowed digits.
        """
        # Create a list and a set with the string of digits. Only if their
        # lengths are equal it means that the digits are different.
        # Only digits contained in the sequence self. seq are allowed.
        if  len(set(s)) == len(list(s)):
            for dig in s:
                if dig not in str(self.seq):
                    return False
            return True
        else:
            return False
            
            
    def create_sequence(self, n):
        """
        Create the integer that contains the sequence of digits required, 
        in reversed order.
        E.g.: If n = 9, then the sequence will be 987654321.
        """
        return int("".join([str(i) for i in range(n, 0, -1)]))
        

    def find_pandigitals(self, seq):
        """
        Find the pandigital products.
        """
        diff_idents = []   
        for mult1 in range(1, int(math.sqrt(self.seq)) + 1):
            for mult2 in range(1, self.seq):
                prod = mult1 * mult2
                ident = str(mult1) + str(mult2) + str(prod)
                
                if prod > self.seq:
                    # Break when the obtained product is bigger than the
                    # maximum allowed number.
                    break
                if len(ident) < 9:
                    continue
                elif len(ident) == 9:
                    # Check if the product is a pandigital product.
                    if self.has_diff_digits(ident):
                        # if a pandigital product is found, create a list 
                        # containing the multiplicand, the multiplier and
                        # the product and append it to the list that will
                        # be returned, if the product isn't yet in the list.
                        if (sorted([mult1, mult2, prod]) not in diff_idents) \
                        and (prod not in [i[2] for i in diff_idents]):
                            diff_idents.append(sorted([mult1, mult2, prod]))
                            print(ident, "\t", mult1, "\t", mult2, "\t", prod)
                else:
                    break
        return diff_idents


if __name__ =='__main__':
    """
    Test the class.
    """ 
    Pandigital_Products(9)