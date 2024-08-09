# Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] to a string using ‘&’. The sample output of this string will be:

# Pythons syntax is easy to learn & Pythons syntax is very clear

import ast,sys
input_str = (sys.stdin.read()).split(',')

string_1 = input_str[0] + ' & ' + input_str[1]
print(string_1)