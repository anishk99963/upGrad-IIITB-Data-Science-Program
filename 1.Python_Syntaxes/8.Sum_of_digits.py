# Write a program to calculate the sum of the digits of a given number 
# ----------------------------------------------------------------------
# Input:An n digit number

# Output:Sum of the digits
# ----------------------------------------------------------------------
# Sample input:983

# Sample output:20
# ----------------------------------------------------------------------
# Sample input:5241

# Sample output:12

def getSum(n):
 
    sum = 0
    while (n != 0):
 
        sum = sum + int(n % 10)
        n = int(n/10)
 
    return sum

n=int(input())
print(getSum(n))