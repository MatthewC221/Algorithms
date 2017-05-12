#!/usr/bin/python

import sys

# All of the subsets of a set! Using the trick that is,
# the subsets of a st are all permutations of the binary number 000 -> 111 for length 3
# 001, 010, 011, 100, 101, 110, 111, 000
# 003, 020, 023, 100, 103, 120, 123, 000
# {3}, {2}, {23}, {1}, {13}, {12}, {123}, {}

def subsets(sequence, total, permutations, total_sum):
    
    if (permutations == total):
        print "The sum of all subsets is = " + str(total_sum)
        return
    
    print "{",
    for i in range(0, len(sequence)):
        if (sequence[i] == 1):
            print (str(i + 1)),
            total_sum += (i + 1)
    print "}"
    
    for i in range(len(sequence) - 1, -1, -1):
        if (sequence[i]):
            sequence[i] = 0
        else:
            sequence[i] = 1
            break
    
    subsets(sequence, total, permutations + 1, total_sum)

if (len(sys.argv) != 2):
    print ("Usage ./subset.py <range>")
else:
    num = [0] * int(sys.argv[1]) 
    total = pow(2, len(num))
    subsets(num, total, 0, 0)
