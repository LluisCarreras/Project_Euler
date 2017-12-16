# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 01:15:28 2016

@author: Lluís Carreras González

Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For 
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?
"""

def words(my_file):
    """
    Return a list with the string items in the given file
    """
            
    return [x[1:-1] for x in open(my_file, 'r').read().strip().split(",")]
                
                
def letter_value(letter):
    """
    Return the letter value of the given letter.
    """
    
    return ord(letter) - ord('A') + 1
    
    
def word_value(word):
    """
    Return the word value of the given word.
    """
    
    the_sum = 0
    for letter in word:
        the_sum += letter_value(letter)
    return the_sum
    
    
triangle_nums = [int(0.5 * n * (n + 1)) for n in range(1, 100)]

the_words = words('p042_words.txt')

count = 0
for word in the_words:
    if word_value(word) in triangle_nums:
        count += 1

print(count)
        



        
       
