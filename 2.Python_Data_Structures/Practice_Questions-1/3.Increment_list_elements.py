# Given a list of strings, increment the value of the numeric strings by 'k’. 
# Hint: The function isdigit() may be useful here.
# --------------------------------------------------------------------------------------------
# Input - A list in the first line and an integer in the second line

# Output - A list
# ---------------------------------------------------------------------------------------------
# Sample Input :
# ['Python', '123', 'Data']
# 4

# Sample Output : ['Python', '127', 'Data']
# ---------------------------------------------------------------------------------------------
# Sample Input :
# ['upGrad', '1991', 'Mumbai']
# 0

# Sample Output : ['upGrad', '1991', 'Mumbai']
# ---------------------------------------------------------------------------------------------
# Sample Input :
# ['Data Science', '100', '10']
# 10

# Sample Output : ['Data Science', '110', '20']

import ast
input_list = ast.literal_eval(input())
K = int(input())
L = []

for i in input_list:
    if i.isdigit():
        i = str(int(i)+int(K))
        L.append(i)
    else:
        L.append(i)
print(L)