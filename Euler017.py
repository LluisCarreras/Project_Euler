# -*- coding: utf-8 -*-
"""
Created on Sun Dec  17 14:01:37 2017
@author: Lluís Carreras González

Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
20 letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""


units_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", 
         "nine"]
teenagers_list = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                    "seventeen", "eighteen", "nineteen"]
tenths_list = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


number_letter_counts = {}

for number in range(1, 1001):
    
    if number < 10:
        number_letter_counts[number] = units_list[number]
        
    elif number < 20:
        number_letter_counts[number] = teenagers_list[number - 10]
        
    elif number < 100:
        tenths = number // 10
        units = number % 10
        number_letter_counts[number] = tenths_list[tenths] + units_list[units]
        
    elif number < 1000:
        hundreds = number // 100
        tenths = (number // 10) % 10
        units = number % 10
        number_in_letters = units_list[hundreds] + "hundred"
        if tenths or units:
            number_in_letters += "and" + number_letter_counts[10 * tenths + units]
        number_letter_counts[number] = number_in_letters
        
    elif number == 1000:
        number_letter_counts[1000] = "onethousand"
 
       
total_count = sum([len(value) for key, value in number_letter_counts.items()])
print(total_count)
        
#print(len(number_letter_counts))
#print(number_letter_counts)
