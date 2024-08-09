# Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria] using list comprehensions.

# Sample Input:['wood','old','apple','big','item','euphoria']

# Sample Output:['old', 'apple', 'item', 'euphoria']

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
v = ['a','e','i','o','u']
list_vowel = [i for i in input_list if i[0] in v]

print(list_vowel)