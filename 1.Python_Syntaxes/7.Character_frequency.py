# Write a program to accept a string value from the user and accept a char value from the user and find out the total occurrence of the char value in the string value. Note that the count is not case-sensitive
# ----------------------------------------------------------------------
# Input:A string and a character whose occurrence is to be found

# Output:An integer
# ----------------------------------------------------------------------
# Sample input:
# Python Programming
# P

# Sample output:2
# ----------------------------------------------------------------------
# Sample input:
# This is my first program
# t

# Sample output:2

# Take input
input_string=input()
input_char=input()
count = 0
for i in input_string:
    if input_char == i:
        count += 1

print(count)