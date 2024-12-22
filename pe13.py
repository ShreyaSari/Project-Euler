n=int(input().strip())
sum_d = 0
for i in range(n):
    a= int(input().strip())
    sum_d+=a
result = str(sum_d)[:10]
print(result)


# Steps to Solve
# 1.Input Parsing:
#   	    First, read the number of lines (nnn).
#           Next, read nnn lines, each containing a 50-digit number.
# 2.Summing the Numbers:
#           Since Python handles large integers using arbitrary-precision, we can directly sum these numbers without needing special techniques.
# 3.Extracting the First 10 Digits:
#           Convert the sum to a string and take the first 10 characters.
# 4.Output:
#           Print these first 10 digits.

# Complexity
# 1.	Time Complexity:
# Reading and summing nnn numbers takes O(n)O(n)O(n).
# Extracting the first 10 digits is O(1)O(1)O(1).
# 2.	Space Complexity:
# Space is used only for the total sum and input, so O(n)O(n)O(n).




#:D yay!