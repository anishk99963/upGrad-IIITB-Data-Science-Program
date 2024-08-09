# Create a function squared(), which takes x and y as arguments and returns the x**y value. For e.g., if x = 2 and y = 3 , then the output is 8.

# Sample Input:['6','7']

# Sample Output:279936


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
x = int(input_list[0])
y = int(input_list[1])

#Write your code here
def squared(a,b):
    return a**b

print(squared(x,y))