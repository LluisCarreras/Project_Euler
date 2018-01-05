# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:44:16 2017
@author: Lluís Carreras

Counting Sundays
Problem 19 

You are given the following information, but you may prefer to do some 
research for yourself.
•1 Jan 1900 was a Monday.
•Thirty days has September,
 April, June and November.
 All the rest have thirty-one,
 Saving February alone,
 Which has twenty-eight, rain or shine.
 And on leap years, twenty-nine.
•A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)?

"""


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


#test_years = [100, 400, 1000, 2000, 2001, 2004]  
#for year in test_years:
#    print(year, is_leap_year(year))    

year = 1901
month = 1
day = 0
total_sundays = 0

# The 1 Jan 1901 was Monday
day_of_week = 1
        
while True:
#    print(year, month, day, total_sundays)
    day += 1
    day_of_week = (day_of_week + 1) % 7
      
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
            if year >= 2001:
                break
    elif month in [4, 6, 9, 11] and day > 30:
        day = 1
        month += 1
    elif month == 2:
        if is_leap_year(year):
            if day > 29:
                day = 1
                month += 1
        else:
            if day > 28:
                day = 1
                month += 1
    if day == 1 and day_of_week == 0:
        total_sundays += 1  
        
  
print(total_sundays)  

###############
# SOLUTION: 171
############### 
