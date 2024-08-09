# Write a program to accept three sides of a triangle as the input and print whether the triangle is valid or not.
# (A triangle is valid if the sum of any two sides is greater than the third side.)
# ----------------------------------------------------------------------
# Input:Three sides of a triangle separated by a space

# Output:Whether the given triangle is "Valid" or "Invalid"
# ----------------------------------------------------------------------
# Sample input:3 4 5

# Sample output:Valid
# ----------------------------------------------------------------------
# Sample input:1 4 5

# Sample output:Invalid

def is_valid_triangle(a,b,c):
    if (a+b<=c and b+c<=a and c+a<=b):
        return False
    else:
        return True

a,b,c= input().split()
if is_valid_triangle(a, b, c):
    print('Valid')
else:
    print('Invalid')