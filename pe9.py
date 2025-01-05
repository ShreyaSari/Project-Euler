#!/bin/python3

import sys

# Function to find the maximum product of a Pythagorean triplet for a given n
def find_max_pythagorean_triplet_product(n):
    max_product = -1
    # Iterate over possible values of m
    for m in range(2, int(n ** 0.5) + 1):
        if n % (2 * m) == 0:
            k = n // (2 * m)
            # Iterate over possible values of n
            for n_val in range(1, m):
                if (m - n_val) % 2 == 1 and m > n_val and k % (m + n_val) == 0:
                    d = k // (m + n_val)
                    a = d * (m * m - n_val * n_val)
                    b = d * (2 * m * n_val)
                    c = d * (m * m + n_val * n_val)
                    max_product = max(max_product, a * b * c)
    return max_product

# Read input values
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(find_max_pythagorean_triplet_product(n))



# explanation:
# ✅ What is a Pythagorean Triplet?
# A Pythagorean triplet is a set of three natural numbers (a, b, c) that satisfies the condition:
# a2+b2=c2a^2 + b^2 = c^2a2+b2=c2
# And we are given that:
# a+b+c=na + b + c = na+b+c=n
# Your task is to find the maximum product a×b×ca \times b \times ca×b×c for a given nnn, or return -1 if no such triplet exists.
# ________________________________________
# ✅ Brute Force vs. Optimized Approach
# 🔴 Brute Force Approach
# •	You iterate over possible values of aaa and bbb, calculate c=n−a−bc = n - a - bc=n−a−b, and check if a2+b2=c2a^2 + b^2 = c^2a2+b2=c2.
# •	This is slow because it requires checking many combinations.
# ________________________________________
# 🟢 Optimized Approach Using Number Theory
# In mathematics, Pythagorean triplets can be generated using two numbers, m and n (where m>nm > nm>n), as follows:
# a=m2−n2a = m^2 - n^2a=m2−n2 b=2×m×nb = 2 \times m \times nb=2×m×n c=m2+n2c = m^2 + n^2c=m2+n2
# The sum of these triplets is:
# a+b+c=2×m×(m+n)a + b + c = 2 \times m \times (m + n)a+b+c=2×m×(m+n)
# ________________________________________
# ✅ Deriving the Formula
# Given a+b+c=na + b + c = na+b+c=n, we can express:
# n=2×m×(m+n)n = 2 \times m \times (m + n)n=2×m×(m+n)
# From this, we can solve for possible values of mmm and nnn.
# ________________________________________
# ✅ Steps in the Code
# 1.	Iterate over possible values of m (starting from 2 up to n\sqrt{n}n).
# 2.	Check if n is divisible by 2×m2 \times m2×m — if not, skip this m.
# 3.	Solve for k = n // (2 \times m).
# 4.	Find values of n_val (smaller than m) that satisfy:
# o	m>nvalm > n_valm>nval
# o	(m−nval)%2==1(m - n_val) \% 2 == 1(m−nval)%2==1 (to ensure one is even, the other odd).
# 5.	Calculate the triplet values using the formulas:
# a=d×(m2−n2),b=d×(2×m×n),c=d×(m2+n2)a = d \times (m^2 - n^2), \quad b = d \times (2 \times m \times n), \quad c = d \times (m^2 + n^2)a=d×(m2−n2),b=d×(2×m×n),c=d×(m2+n2)
# 6.	Keep track of the maximum product a×b×ca \times b \times ca×b×c.
# ________________________________________
# ✅ Code Walkthrough
# Let's say n=12n = 12n=12.
# Step 1: Check possible values of m
# We iterate from m = 2 to m = 3.
# Step 2: For m = 2, calculate:
# n=12,2×m=4n = 12, \quad 2 \times m = 4n=12,2×m=4 k=12//4=3k = 12 // 4 = 3k=12//4=3
# Step 3: Check possible values of n_val
# For nval=1n_val = 1nval=1 (since nval<mn_val < mnval<m), calculate:
# a=3×(4−12)=3×3=9a = 3 \times (4 - 1^2) = 3 \times 3 = 9a=3×(4−12)=3×3=9 b=3×(2×2×1)=3×4=12b = 3 \times (2 \times 2 \times 1) = 3 \times 4 = 12b=3×(2×2×1)=3×4=12 c=3×(4+12)=3×5=15c = 3 \times (4 + 1^2) = 3 \times 5 = 15c=3×(4+12)=3×5=15
# ________________________________________
# ✅ Why is This Faster?
# Instead of brute-forcing all possible triplets, we:
# 1.	Reduce the search space by focusing on m and n.
# 2.	Use mathematical properties of Pythagorean triplets to generate valid combinations efficiently.
# ________________________________________
# ✅ Sample Input/Output Explanation
# Input	Output	Explanation
# 12	60	Triplet (3, 4, 5) gives product 3×4×5=603 \times 4 \times 5 = 603×4×5=60.
# 4	-1	No valid triplet exists for n=4n = 4n=4.
# ________________________________________
# ✅ Why Use the Formula?
# Because Pythagorean triplets follow a predictable pattern, we can generate them using the formulas for aaa, bbb, and ccc, instead of randomly searching for triplets.

