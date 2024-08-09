# Using the Reduce function, concatenate a list of words in input_list, and print the output as a string.
# If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.

# Sample Input:['All','you','have','to','fear','is','fear','itself']

# Sample Output:All you have to fear is fear itself


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

from functools import reduce

result=reduce(lambda x,y: x+" "+y, input_list)

print(result)