# In ‘ABC’ university, company ‘XYZ’ conducted three rounds of interviews to recruit students. Those students who passed all the rounds were selected. The company released the results for each round in a separate list. Your task is to write a Python code to display the list of the students who passed all the three rounds.
# Note: a. Name of the person can be given in uppercase or lowercase.
# b. Print the names in lowercase in the output.

# Input: 
# List
# List
# List

# Output: List
# ----------------------------------------------------------------------
# Sample input: 
# ['Arkam', 'Bairstow', 'Cairy', 'Darpan'] 
# ['ARKAM', 'Bairstow', 'Cairy', 'Darpan', 'Dhoni', 'Sachin']
# ['arkam', 'bairstow', 'Cheteshwar', 'Dinesh']
     
# Sample output: ['arkam', 'bairstow']
# ----------------------------------------------------------------------
# Sample input: 
# ['Pranay', 'Aditya', 'Deepesh', 'Sandesh']
# ['Pranoy', 'Surya', 'Cairy', 'Vignesh', 'ADITYA', 'SANDesh']
# ['Vardhan', 'Shailesh', 'aditya', 'sandesh']
      
# Sample output: ['aditya', 'sandesh']
# ----------------------------------------------------------------------
# Sample input: 
# ['Siddharth', 'Gaurav', 'Prasad', 'Kuldeep', 'karna']
# ['siddharth', 'Gaurav', 'Prasad', 'Kuldeep', 'karna']
# ['Siddharth', 'gaurav', 'PRASAD', 'KuLDEEp', 'KARNA']

# Sample output: ['siddharth', 'gaurav', 'prasad', 'kuldeep', 'karna']

import ast
list1 = ast.literal_eval(input())
list2 = ast.literal_eval(input())
list3 = ast.literal_eval(input())

R1 = list(map(lambda x: x.lower(),list1))
R2 = list(map(lambda x: x.lower(),list2))
R3 = list(map(lambda x: x.lower(),list3))

final_list = []
for i in R1:
    if (i in R2) and (i in R3):
        final_list.append(i)

print(final_list)