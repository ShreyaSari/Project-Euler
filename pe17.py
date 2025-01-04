# Enter your code here. Read input from STDIN. Print output to STDOUT

# Dictionaries for number to word mapping
numbers = {
    0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}
teens = {
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}
tens = {
    20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
    60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
}

# Function to convert numbers to words
def convert(n):
    if n == 0:
        return "Zero"
    elif n < 10:
        return numbers[n]
    elif n < 20:
        return teens[n]
    elif n < 100:
        return tens[n // 10 * 10] + (" " + numbers[n % 10] if n % 10 != 0 else "")
    elif n < 1000:
        return numbers[n // 100] + " Hundred" + (" " + convert(n % 100) if n % 100 != 0 else "")
    elif n < 1000000:
        return convert(n // 1000) + " Thousand" + (" " + convert(n % 1000) if n % 1000 != 0 else "")
    elif n < 1000000000:
        return convert(n // 1000000) + " Million" + (" " + convert(n % 1000000) if n % 1000000 != 0 else "")
    else:
        return convert(n // 1000000000) + " Billion" + (" " + convert(n % 1000000000) if n % 1000000000 != 0 else "")

# Read input and print output
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(convert(n).strip())


#================================================================================================

# the below code is written by my own and the above code is from the hacker rank




# ones = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
# teens = {10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
# tens = {20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety", 100:"Hundred"}

# def convert(n):
# /*************  ✨ Codeium Command ⭐  *************/
#     """
#     Converts a given number to its word representation.

#     Parameters:
#     n (str|int): The number to be converted.

#     Returns:
#     str|int: The word representation of the given number.

#     Examples:
#     >>> convert(1)
#     "One"
#     >>> convert(12)
#     "Twelve"
#     >>> convert(45)
#     "Forty-Five"
#     >>> convert(123)
#     "One Hundred Twenty-Three"
#     >>> convert(1000)
#     "Number out of range"
#     >>> convert("Zero")
#     0
#     """
    
# /******  7a095bf7-0087-4d4d-8228-452a7f3993dd  *******/
#     if n == "Zero":
#         return 0;
#     elif n<10:
#         return ones[n]
#     elif n<20:
#         return teens[n]
#     elif n < 100:
#         return tens[(n // 10) * 10] + ("-" + ones[n % 10] if n % 10 != 0 else "")
#     elif n < 1000:
#         return ones[n // 100] + " Hundred" + (" " + convert(n % 100) if n % 100 != 0 else "")
#     else:
#         return "Number out of range"

# t=int(input().strip())
# for _ in range(t):
#     n=int(input().strip())
#     print(convert(n).strip())


# explanation:
