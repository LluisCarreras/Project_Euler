# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:17:57 2016
@author: Lluís Carreras González

Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a 
name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
 would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def sorted_names(my_file):
    """
    Returns a sorted list with the string items in the given file
    """
            
    return sorted([x[1:-1] 
            for x in open(my_file, 'r').read().strip().split(",")])
 

def score(list_of_names):
    """
    Returns the total sum of the values obtained multiplying the alphabetical 
    order for each name by its alphabetical position.
    
    """
    
    list_total = 0
    for name in list_of_names:
        position = list_of_names.index(name) + 1
        name_value = 0
        for char in name:
            name_value += ord(char) - ord('A') + 1
        score = position * name_value
        list_total += score
    return list_total            
            
#print(sorted_names("p022_names.txt"))  
#print(ord('A'))
            
print(score(sorted_names("p022_names.txt")))
