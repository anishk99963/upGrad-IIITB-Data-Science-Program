# A company stores the names of their employees in a list. They want to encrypt the names so that no one can read them and the data stays safe. One of the steps in encrypting is to reverse each name in the list and convert them to uppercase and your task is to write a Python code to execute the same.
# Note: Use lambda and map functions.

# Input: A list of names

# Output: A list of encrypted names
# ----------------------------------------------------------------------
# Sample input: ['Ronaldo', 'Cristiano', 'Rakesh', 'Ronak']

# Sample output: ['ODLANOR', 'ONAITSIRC', 'HSEKAR', 'KANOR']
# ----------------------------------------------------------------------
# Sample input: ['Abhay', 'Aravind', 'Desilva', 'Darpan']

# Sample output: ['YAHBA', 'DNIVARA', 'AVLISED', 'NAPRAD']

import ast
input_list = ast.literal_eval(input())
output_list = list(map(lambda x: x.upper()[::-1],input_list))
print(output_list)