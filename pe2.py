# Function to calculate the sum of even Fibonacci numbers up to a given limit
def sum_even_fibonacci(limit):
    """
    Calculate the sum of even-valued Fibonacci numbers not exceeding the limit.

    Parameters:
    limit (int): The maximum value a Fibonacci number can have.

    Returns:
    int: Sum of even Fibonacci numbers up to the limit.
    """
    # Initialize the first two Fibonacci numbers
    a, b = 1, 2
    even_sum = 0  # Initialize the sum of even-valued terms

    # Generate Fibonacci numbers until the current number exceeds the limit
    while b <= limit:
        if b % 2 == 0:  # Check if the number is even
            even_sum += b  # Add the even Fibonacci number to the sum
        a, b = b, a + b  # Generate the next Fibonacci number

    return even_sum  # Return the total sum of even Fibonacci numbers


# Input handling
t = int(input().strip())  # Number of test cases
for _ in range(t):
    n = int(input().strip())  # Upper limit for the Fibonacci sequence
    print(sum_even_fibonacci(n))  # Print the result for each test case




# example workflow
# Input: 
# 𝑛 = 10
# n=10
# Initialize:
# a = 1, b = 2, \text{even_sum} = 0
# Loop:
# 𝑏=2
# b=2 (even): Add to even_sum → \text{even_sum} = 2
# Update: 
# 𝑎=2,𝑏=3
# a=2,b=3
# 𝑏=3
# b=3 (odd): Skip
# Update: 
# 𝑎=3,𝑏=5
# a=3,b=5
# 𝑏=5
# b=5 (odd): Skip
# Update: 
# 𝑎=5,𝑏=8
# a=5,b=8
# 𝑏=8
# b=8 (even): Add to even_sum → \text{even_sum} = 10
# Update: 
# 𝑎=8,𝑏=13
# a=8,b=13 (exit loop as 𝑏>𝑛b>n)
# Return:
# \text{even_sum} = 10
# Output: 10
# Complexity Analysis
# Time Complexity:

# Each Fibonacci number is calculated once, up to the given limit 𝑛n. This is 𝑂(log𝑛)
# O(logn), as Fibonacci numbers grow exponentially.
# Space Complexity:

# Only a few variables (a, b, even_sum) are used, so the space complexity is 𝑂(1)
# O(1).