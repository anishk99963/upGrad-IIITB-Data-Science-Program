# Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK' in its place.

# Sample Input:['SAS', 'R', 'PYTHON', 'SPSS']

# Sample Output:['SAS', 'R', 'PYTHON', 'SPARK']

import ast,sys
input_list = (sys.stdin.read()).split(',')
# Write code to remove 'SPSS'
input_list.pop()
# Write code to append 'SPARK'
input_list.append('SPARK')
print(input_list)