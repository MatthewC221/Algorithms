#!/usr/bin/python

# Largely inspired by others online, however this is the first permutation I truly understood, takes
# lots of extra space though...

import sys
import math

if (len(sys.argv) == 2):
    start = [[]]
    perm = sys.argv[1]
    
    count = 0
    for char in perm:
        new = []
        for cur in start:
            for k in range(len(cur) + 1):
                if (len(cur) == len(perm) - 1):
                    print (cur[k:] + [char] + cur[:k])
                    count += 1
                else:
                    new.append(cur[k:] + [char] + cur[:k])
        start = new
    
    assert(math.factorial(len(perm) == count))
    print "Count is " + str(count)
    
else:
    print "Usage ./permute.py <string>"
