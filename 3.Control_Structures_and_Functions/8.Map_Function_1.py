# Create a list ‘name’ consisting of the combination of the first name and the second name from list 1 and 2 respectively. 

# For e.g. if the input list is:[ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]

# the output list should be the list:['Ankur Narang', 'Avik Sarkar', 'Kiran R', 'Nitin Sareen']

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
first_name = input_list[0]
last_name = input_list[1]

combine=lambda x,y:x+' '+y
name = list(map(combine,first_name,last_name))

print(name)