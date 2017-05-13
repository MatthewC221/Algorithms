#!/usr/bin/python

import sys
import random
import time

# Maximum value contiguous subsequence
# I'm not really understanding DP in algorithms right now, so I need to practice DP

def max_subsequence(A):

    max_sum = 0
    
    for i in range(1, len(A)):
        A[i] = max(A[i - 1] + A[i], A[i])
        
        if (A[i] > max_sum):
            max_sum = A[i]            
            
    print ("Max subsequence sum = " + str(max_sum))

if (len(sys.argv) != 2):
    print ("Usage ./longest_subsequence.py <size>")
else:
    random.seed(time.time())
    size = int(sys.argv[1])
    
    A = []
    for i in range(0, size):
        A.append(random.randint(-100, 100))
    
    print A 
    max_subsequence(A)



