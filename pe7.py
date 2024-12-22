#!/bin/python3

import sys
import math

# Function to generate primes using the Sieve of Eratosthenes
def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    primes = []
    
    # Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Collecting prime numbers
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes

# Function to get the n-th prime
def nth_prime(n, primes):
    return primes[n - 1]

# Main script
t = int(input().strip())
max_n = 0
cases = []

# Collect all input cases and find the maximum n needed
for _ in range(t):
    n = int(input().strip())
    cases.append(n)
    max_n = max(max_n, n)

# Estimate an upper limit for the sieve to ensure enough primes
# Using approximation: n * (ln(n) + ln(ln(n))) for large n
if max_n >= 6:
    upper_limit = int(max_n * (math.log(max_n) + math.log(math.log(max_n))))
else:
    upper_limit = 15  # A small limit to cover cases like n=1 to n=6

# Generate primes up to the estimated limit
primes = generate_primes(upper_limit)

# Print results for each test case
for n in cases:
    print(nth_prime(n, primes))



#-------------------------------------------------------------------------------------

#code 2

#!/bin/python3

import sys
import math

# Function to generate primes using the Sieve of Eratosthenes
def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    primes = []
    
    # Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Collecting prime numbers
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes

# Function to get the n-th prime
def nth_prime(n, primes):
    return primes[n - 1]

# Main script
t = int(input().strip())
max_n = 0
cases = []

# Collect all input cases and find the maximum n needed
for _ in range(t):
    n = int(input().strip())
    cases.append(n)
    max_n = max(max_n, n)

# Estimate an upper limit for the sieve to ensure enough primes
# Using approximation: n * (ln(n) + ln(ln(n))) for large n
if max_n >= 6:
    upper_limit = int(max_n * (math.log(max_n) + math.log(math.log(max_n))))
else:
    upper_limit = 15  # A small limit to cover cases like n=1 to n=6

# Generate primes up to the estimated limit
primes = generate_primes(upper_limit)

# Print results for each test case
for n in cases:
    print(nth_prime(n, primes))
