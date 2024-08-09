# Write a program to accept a string from the user, delete all vowels from the string and display the result. 
# ----------------------------------------------------------------------
# Input:A string

# Output:A string with vowels removed
# ----------------------------------------------------------------------
# Sample input:Upgrad

# Sample output:pgrd
# ----------------------------------------------------------------------

# Sample input:Python Programming

# Sample output:Pythn Prgrmmng

# Take input
s=input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(s)):
    if s[i] not in vowels:
        result = result + s[i]

print(result)