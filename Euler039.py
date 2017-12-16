# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:04:40 2016

@author: Lluís

Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math


def get_hypotenuse(side1, side2):
    """
    Create right angle triangle given both rigth angle sides.
    Return the hypotenuse.
    """
    
    return math.sqrt(math.pow(side1, 2) + math.pow(side2, 2))
    
    
def is_integral(num):
    """
    Evaluate wether the given number is integral.
    """
    
    return not (num - int(num) > 0.0)
  
  
def get_perimeter(side1, side2, side3):
    """
    Return the perimeter of a triangle given the three sides.
    """
    
    return side1 + side2 + side3
    
    
def get_num_solutions(perimeter):
    """
    Return the number of solutions for a given perimeter.
    """
    solutions = []
    for side1 in range(1, perimeter - 1):
        for side2 in range(1, perimeter - 1):
            hypotenuse = get_hypotenuse(side1, side2)
            new_perimeter = get_perimeter(side1, side2, hypotenuse)
            if new_perimeter > perimeter:
                break
            if is_integral(hypotenuse):               
                sides = sorted([side1, side2, int(hypotenuse)])
                if new_perimeter == perimeter and sides not in solutions:
                    solutions.append(sides)
    return len(solutions)


def get_solution(max_perim):
    """
    Calculates the solution to the problem for the given maximum perimeter.
    Return a tuple where the first item is the number at which the number of 
    solutions is maximized and the second item is this maximum number of 
    solutions.
    """
    
    max_num_solutions = 0
    max_solution = 0    
    for n in range(3, max_perim + 1):
        #print("Iteration: ", n)
        num_solutions = get_num_solutions(n)
        if num_solutions > max_num_solutions:
            max_num_solutions = num_solutions
            max_solution = n
            print("Perimeter: ", n, "\tNumber of solutions", num_solutions)
    return max_solution, max_num_solutions


solution = get_solution(1000)            
print("\npMAX:                        ", solution[0])
print("Maximum number of solutions: ", solution[1])


    
#print(get_num_solutions(120))
                
            
            
            
    
    

        