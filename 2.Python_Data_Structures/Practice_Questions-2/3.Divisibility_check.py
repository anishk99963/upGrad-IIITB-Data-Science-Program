# Given an integer ‘n’, your task is to write a Python code to find whether ‘n’ is divisible by all its digits or not. If they divide the number, then the number ‘n’ is a happy number. Otherwise, it is a sad number.

# The number ‘n’ may be provided with commas. At first, you have to clean the number (by removing the commas involved) and then check whether the number is happy or sad.
# ---------------------------------------------------------------------------------------------------
# Input - String

# Output - String
# ---------------------------------------------------------------------------------------------------
# Sample Input - 2,128

# Sample Output - Happy Number
# ---------------------------------------------------------------------------------------------------
# Sample Input - 256

# Sample Output - Sad Number
# ---------------------------------------------------------------------------------------------------
# Sample Input - 1124

# Sample Output - Happy Number


# Take input as a string
str1 = input().strip()
str1 = str1.replace(",","")
num1 = int(str1)
flag = 1
for char in str1:
    temp = int(char)
    if temp == 0 or num1 % temp != 0:
        flag = 0
        break
        
if flag == 1:
    print("Happy Number")
else:
    print("Sad Number")