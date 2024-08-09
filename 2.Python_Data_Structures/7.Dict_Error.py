# From a Dictionary input_dict={'Name': 'Monty', 'Profession': 'Singer' }, get the value of a key ‘Label’ which is not a part of the dictionary, in such a way that Python doesn't hit an error. If the key does not exist in the dictionary, Python should return 'NA'.

# Sample Input:{'Name': 'Monty', 'Profession': 'Singer' }

# Sample Output:NA

import ast,sys
input_str = sys.stdin.read()
input_dict = ast.literal_eval(input_str)
def f(inp):
    for i in inp.keys():
        if i != 'Label':
            return 'NA'
answer=f(input_dict)