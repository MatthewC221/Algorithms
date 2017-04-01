#!/usr/bin/python

import sys

# This was in my codility assessment. If you are from codility feel free to tell me to take this down
# We had to debug this program, the question works:

"""
You get A[] of ints, K is the number of times you can nail something down, you can't raise a number
e.g.

with A[1,2,3,4,5] and K = 4
We can nail 2,3,4,5 to 1. Therefore the result is 5 (max things of the same height)

[1, 1, 1, 1, 1] and K = 0, Result = 5

"""

def solution(A, K):
    n = len(A)
    best = int(n - K - 1 == 0)
    count = 1
    
    
    for i in xrange(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
           count = 1
        best = max(best, count) 
    result = best + K


    return result

"""
A = [1, 5, 5, 5, 5, 5]
print solution(A, 6)

A = [1, 1, 1, 1, 1, 2]
print solution(A, 3)

A = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
print solution(A, 2)

A = [1, 1, 2, 2, 3, 3]
print solution(A, 4)

A = [1, 2, 3]
print solution(A, 2)

A = [1, 1, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
print solution(A, 3)

A = [1]
print solution(A, 0)

A = [1, 2]
print solution(A, 1)
"""
