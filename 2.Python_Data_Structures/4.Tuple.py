# Add the element ‘Python’ to a tuple input_tuple = ('Monty Python', 'British', 1969). Since tuples are immutable, one way to do this is to convert the tuple to a list, add the element, and convert it back to a tuple.

# Sample Input:('Monty Python', 'British', 1969)

# Sample Output:('Monty Python', 'British', 1969, 'Python')

import ast,sys
input_str = sys.stdin.read()
input_tuple = ast.literal_eval(input_str)

# Write your code here
temp = list(input_tuple)
temp.append('Python')
tuple_2 = tuple(temp)
# Make sure to name the final tuple 'tuple_2'
print(tuple_2)