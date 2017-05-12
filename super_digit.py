#!/usr/bin/python3

"""
Practicing recursion

We define super digit of an integer X using the following rules:

If X has only  digit, then its super digit is X.
Otherwise, the super digit of X is equal to the super digit of the digit-sum of X. 
"""

import sys

def super_digit(num):

    # Base case
    if (len(num) == 1):
        return
    
    temp_sum = sum(num)
    new_num = [int(x) for x in str(temp_sum)] 
    
    print (new_num)    
    return super_digit(new_num)

n, k = input().split(' ')
k = int(k)
d = list(map(int, (n * k)))
print (d)

super_digit(d)

