# Write a program to accept a number from the user and count the zeros, odd digits and non-zero even digits from the entered number.
# ----------------------------------------------------------------------
# Input:A positive integer of n digits

# Output:Three integers representing the occurrences of zeros, odd digits and non-zero even digits from the entered number.
# ----------------------------------------------------------------------
# Sample input:1030

# Sample output:
# Number of odd digits: 2
# Number of non-zero even digits: 0
# Number of zeros: 2

def getcount(n,count_zero,count_even,count_odd):
    while n != 0:
        temp = int(n%10)
        if(temp%2==0 and temp != 0):
            count_even += 1
        elif(temp%2!=0):
            count_odd += 1
        elif(temp == 0):
            count_zero += 1
        n = int(n/10)    
    
    print('Number of odd digits:', count_odd)
    print('Number of non-zero even digits:', count_even)
    print('Number of zeros:', count_zero)

n=int(input())
count_odd = 0;
count_even = 0;
count_zero = 0;
getcount(n,count_zero,count_even,count_odd)