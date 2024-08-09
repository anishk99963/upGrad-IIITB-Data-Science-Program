# Split the string input_str = 'Kumar_Ravi_003' to the person's second name, first name and unique customer code. In this example, second_name= 'Kumar', first_name= 'Ravi', customer_code = '003'.

# A sample output of the input 'Kumar_Ravi_003' is:
# Ravi
# Kumar
# 003


import ast,sys
input_str = sys.stdin.read()
temp = input_str.split('_')
first_name = temp[1]
second_name = temp[0]
customer_code = temp[2]
print(first_name)
print(second_name)
print(customer_code)