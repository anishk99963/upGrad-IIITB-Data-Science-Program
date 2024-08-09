# Write a python code to merge two dictionaries into a single dictionary.
# --------------------------------------------------------------------------------------------------
# Input: Two dictionaries, one in each line

# Output: A Dictionary
# --------------------------------------------------------------------------------------------------
# Sample Input :
# {'a': 10, 'b': 8}
# {'d': 6, 'c': 4}

# Sample Output : {'c': 4, 'a': 10, 'b': 8, 'd': 6}
# --------------------------------------------------------------------------------------------------
# Sample Input :
# {'a': 110, 'b': 88}
# {'d': 62, 'c': 44}

# Sample Output : {'a': 110, 'b': 88, 'd': 62, 'c': 44}

import ast

#take input of two dictionaries
dict_1 = ast.literal_eval(input())
dict_2 = ast.literal_eval(input())
dict_1.update(dict_2)
print(dict_1)