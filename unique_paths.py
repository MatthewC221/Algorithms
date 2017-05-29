#!/usr/bin/python

import sys

# Dynamic programming solution to unique paths

def uniq_paths(size):
    
    arr = [[] for x in xrange(size)]
    for i in range(0, len(arr)):
        for j in range(0, size):
            arr[i].append(1)
            
    # Not sure the quickest way to initialise...
    
    # DP, paths to a point is the sum of its top node and its left (unless row = 0, col = 0)
    for i in range(1, size):
        for j in range(1, size):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    
    print ("The number of unique paths is = " + str(arr[size - 1][size - 1]))

if (len(sys.argv) != 2):
    print ("Usage ./unique_paths.py <size>")
else:
    size = int(sys.argv[1])
    uniq_paths(size)
