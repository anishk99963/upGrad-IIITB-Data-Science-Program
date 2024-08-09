# You are given a list of strings such as input_list = ['hdjk', 'salsap', 'sherpa'].

# Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.

# Sample Input:['soap','sharp','shy','silent','ship','summer','sheep']

# Sample Output:['soap', 'sharp', 'ship', 'sheep']

# Note: Use the filter() function.

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

sp = list(filter(lambda x:x[0].lower()=='s' and x[-1]=='p',input_list))

print(sp)