# Function to find the largest prime factor of a given number
def largest_prime_factor(n):
    """
    Finds the largest prime factor of the given number n.

    Parameters:
    n (int): The number for which to find the largest prime factor.

    Returns:
    int: The largest prime factor of n.
    """
    largest_factor = 1  # Variable to store the largest prime factor

    # Step 1: Remove all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2  # Divide n by 2 repeatedly

    # Step 2: Check for odd factors starting from 3
    factor = 3
    while factor * factor <= n:  # No need to check beyond sqrt(n), coz they keep repeating, factors of 36 = (2,18),(3,12),(4,9),(6,6)... after this they keep repeating
        while n % factor == 0:
            largest_factor = factor
            n //= factor  # Divide n by the current factor
        factor += 2  # Increment by 2 to check the next odd number

    # Step 3: If n is still greater than 2, it must be a prime number
    if n > 2:
        largest_factor = n

    return largest_factor


# Input handling
t = int(input().strip())  # Number of test cases
for _ in range(t):
    n = int(input().strip())  # Input number for each test case
    print(largest_prime_factor(n))  # Output the largest prime factor

#expalnation: 


# Complexity Analysis
# 1.	Time Complexity:
# o	Dividing by 2 repeatedly is O(log⁡n)O(\log n)O(logn).
# o	Checking odd factors up to n\sqrt{n}n is approximately O(n)O(\sqrt{n})O(n).
# o	Total complexity: O(n)O(\sqrt{n})O(n).
# 2.	Space Complexity:
# o	Only a few variables are used, so the space complexity is O(1)O(1)O(1).

