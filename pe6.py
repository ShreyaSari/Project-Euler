#!/bin/python3

import sys

def abs_diff(n):
    squared_sum_of_numbers = (n*(n+1)//2)**2
    sum_of_squares = (n*(n+1)*(2*n+1))//6
    diff = abs(squared_sum_of_numbers - sum_of_squares)
    return diff
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(abs_diff(n))




# Explanation of Code:
# 1.	Formula Efficiency:
# o	The formulas for Sum of Squares and Square of Sum eliminate the need for loops, making the solution very efficient, even for large nnn.
# 2.	Function Details:
# o	sum_of_squares: Uses the pre-derived formula n(n+1)(2n+1)6\frac{n(n+1)(2n+1)}{6}6n(n+1)(2n+1) for summing squares of the first nnn numbers.
# o	square_of_sum: Uses (n(n+1)2)2\left(\frac{n(n+1)}{2}\right)^2(2n(n+1))2 for the square of the sum.
# o	abs: Ensures the difference is always non-negative.
# 3.	Iterating Over Test Cases:
# o	We loop through all test cases, call the function, and print the result.




#  :D I wrote it on my own!!