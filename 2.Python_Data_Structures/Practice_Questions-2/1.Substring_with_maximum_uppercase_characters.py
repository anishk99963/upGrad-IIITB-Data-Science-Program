# Given a string, write a Python program to find the largest substring of uppercase characters and print the length of that substring. Check the sample inputs and outputs for a better understanding.
# ---------------------------------------------------------------------------------------------------
# Input - String

# Output - String
# ---------------------------------------------------------------------------------------------------
# Sample Input - I lovE PRogrAMMING

# Sample Output - 6

# Explanation - AMMING is the largest substring with all characters in uppercase continuously 
# -----------------------------------------------------------------------------------------------------
# Sample Input - MuMbaI is in MAHArashTRA

# Sample Output - 4

# Explanation - MAHA is the largest substring with all characters in uppercase continuously.
# ---------------------------------------------------------------------------------------------------
# Sample Input - India WOn the WOrLD CUP

# Sample Output - 3

# Explanation - CUP is the largest substring with all characters in uppercase continuously.

test_str = input().strip()

cnt = 0
res = 0
for idx in range(0, len(test_str)):
    if test_str[idx].isupper():
        cnt += 1
    else:
        if res < cnt:
            res = cnt
        cnt = 0

if res < cnt:
    res = cnt

print(res)