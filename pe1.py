def sum_of_multiples(limit):
    """
    Calculate the sum of all multiples of 3 or 5 below a given limit.

    Parameters:
    limit (int): The number below which multiples are considered.

    Returns:
    int: The sum of all multiples of 3 or 5 below the given limit.
    """
    # Adjust limit to exclude the number itself
    limit -= 1

    # Sum of multiples of 3
    # Using the formula: sum = n * (n + 1) / 2
    # where n is the number of terms (limit // 3)
    sum_3 = 3 * (limit // 3) * (limit // 3 + 1) // 2

    # Sum of multiples of 5
    # Same logic as sum_3 but with multiples of 5
    sum_5 = 5 * (limit // 5) * (limit // 5 + 1) // 2

    # Sum of multiples of 15 (to avoid double-counting)
    # 15 is the LCM of 3 and 5, representing numbers divisible by both
    sum_15 = 15 * (limit // 15) * (limit // 15 + 1) // 2

    # Add multiples of 3 and 5, then subtract the double-counted multiples of 15
    return sum_3 + sum_5 - sum_15
