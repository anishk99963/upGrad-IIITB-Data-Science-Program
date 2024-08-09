# Write a program that takes a string as the input and does the following:
#     -Removes the numbers, special characters
#     -Converts uppercase letters to lowercase letters, and vice versa 
# ----------------------------------------------------------------------
# Input:A string 

# Output:A string with numbers, special characters removed, upper and lower cases swapped
# ----------------------------------------------------------------------
# Sample input:Programming1234

# Sample output:pROGRAMMING
# ----------------------------------------------------------------------
# Sample input: Programming is 100% fun

# Sample output: pROGRAMMINGISFUN

input_string=input()
test_str = ''.join(letter for letter in input_string if letter.isalpha())
test_str = test_str.swapcase()
print(test_str)