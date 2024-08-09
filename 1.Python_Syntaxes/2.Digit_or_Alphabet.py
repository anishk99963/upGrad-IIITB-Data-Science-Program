# Write a program to display whether the input is a digit or a letter of the alphabet.
# ----------------------------------------------------------------------
# Input:
# A digit or a letter of the alphabet

# Output:

# Displays whether the given output is an integer or a letter of the alphabet
# ----------------------------------------------------------------------
# Sample input: 1

# Sample output: Integer
# ----------------------------------------------------------------------
# Sample input: b

# Sample output: Alphabet

# Take input
inp=input()
if((inp>='a' and inp<='z') or (inp>='A' and inp<='Z')):
    print("Alphabet")
elif(inp>='0' and inp<='9'):
    print("Integer")
