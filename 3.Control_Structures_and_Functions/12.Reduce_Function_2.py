# You are given a list of numbers such as input_list = [31, 63, 76, 89]. Find and print the largest number in input_list using the reduce() function.

# Sample Input:[65,76,87,23,12,90,99]

# Sample Output:99

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
from functools import reduce

answer = reduce(lambda x,y: x if x>y else y,input_list)

print(answer)