# Using the function Map, count the number of words that start with ‘S’ in input_list.

# Sample Input:['Santa Cruz','Santa fe','Mumbai','Delhi']

# Sample Output:2

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

count = sum(map(lambda x: x[0] == 'S', input_list))

print(count)