# Write a code to check if the string in input_str starts with a vowel or not. Print capital YES or NO.

# For example, if input_str = 'analytics' then, your output should print 'YES'.

# Sample Input:alpha

# Sample Output:YES

import ast,sys
input_str = sys.stdin.read()
check_v = ['a','e','i','o','u','A','E','I','O','U']
flag = 0
for i in check_v:
    if(input_str[0] == str(i)):
        flag = 1
        

if flag == 1:
    print('YES')
else:
    print("NO")