#!/bin/python3

# Function to calculate the maximum product of k consecutive digits
def max_product(n, k, num):
    max_product = 0
    current_product = 1
    zero_count = 0

    # Convert the number to a list of digits
    digits = list(map(int, num))

    for i in range(n):
        # Add the new digit to the window
        if digits[i] == 0:
            zero_count += 1
        else:
            current_product *= digits[i]

        # Remove the digit that goes out of the window
        if i >= k:
            if digits[i - k] == 0:
                zero_count -= 1
            else:
                current_product //= digits[i - k]

        # Update the maximum product if no zeros are in the current window
        if i >= k - 1 and zero_count == 0:
            max_product = max(max_product, current_product)

    return max_product

# Main logic
t = int(input().strip())  # Number of test cases
for a0 in range(t):
    # Read n (number length) and k (substring length)
    n, k = map(int, input().strip().split(' '))
    # Read the number as a string
    num = input().strip()

    # Calculate and print the result for each test case
    print(max_product(n, k, num))


# explanation:
# we are using the sliding window technique to solve this problem. Keeping a zero_count to track zeros in the current window. If zeros exist, the product of the window is 
# 0, so it is skipped.

# Complexity
# 1.	Time Complexity:
# o	O(n)O(n)O(n) per test case due to a single pass through the digits.
# 2.	Space Complexity:
# o	O(1)O(1)O(1), as we use a few variables to track the product and zeros.

