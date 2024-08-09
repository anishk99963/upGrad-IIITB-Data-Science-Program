# Create a SORTED list of all values from the dictionary input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}

# Sample Input:{'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}

# Sample Output:['Amazon', 'Apple', 'RJIO', 'Twitter']

import ast,sys
input_str = sys.stdin.read()
input_dict = ast.literal_eval(input_str)
value_list = input_dict.values()

print(sorted(value_list))