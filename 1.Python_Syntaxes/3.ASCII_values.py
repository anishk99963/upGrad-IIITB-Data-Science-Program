# Write a program to accept a character and display its next and previous character. 
# Hint: Make use of Ascii values here.
# ----------------------------------------------------------------------
# Input: A character

# Output:Previous character and the next character of the given character
# ----------------------------------------------------------------------
# Sample input: D

# Sample output:
# C
# E
# ----------------------------------------------------------------------
# Sample input: 8

# Sample output:
# 7
# 9
# ----------------------------------------------------------------------
# Sample input: @

# Sample Output: 
# ?
# A

charcter = input()
order_input = ord(charcter)
previous_character = chr(order_input - 1)
next_character = chr(order_input +1 )
print(previous_character)
print(next_character)