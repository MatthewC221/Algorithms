#!/usr/bin/python

import sys
import time

# Iterative normal_search vs recursive binary

# Try running it with a low range first, say 0->100. Then use larger ranges, the difference is huge!
# initially normal_search outperforms binary_search (due to recursion being expensive) in certain 
# languages (C, Java, Python)

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2 - time1) * 1000.0)
        return ret
    return wrap
    
@timing
def bin_search_call(A, upper_bound, lower_bound, target):           # Eliminates multiple @timing calls
    return bin_search(A, upper_bound, lower_bound, target)

def bin_search(A, upper_bound, lower_bound, target):

    # This check is here in case the number is not existent in the array 
    # Change line 56 to: arr = range(0, arr_range, 2), and search for an odd number
    if (upper_bound == lower_bound + 1 and A[lower_bound] != target):
        return -1
    
    middle = (upper_bound + lower_bound) / 2
    if (A[middle] == target):
        return middle
    
    if (A[middle] > target):
        return bin_search(A, middle, lower_bound, target)
    else:
        return bin_search(A, upper_bound, middle, target)

@timing        
def normal_search(A, target):
    
    for i in range(0, len(A)):
        if (A[i] == target):
            return i
    
    return -1

if (len(sys.argv) != 3):
    print ("Usage ./bin_search.py <range> <number>")
else:
    number, arr_range = int(sys.argv[2]), int(sys.argv[1])
    if (number <= 0 or number > arr_range):
        print ("Please enter a non-zero number within the range!")
        sys.exit(0)
    
    arr = range(0, arr_range)
    print ("Performing binary search...")
    index = bin_search_call(arr, arr[len(arr) - 1], arr[0], number)
    print ("Index found at " + str(index) + "\n")
    
    print ("Performing normal search...")
    index = normal_search(arr, number)
    print ("Index found at " + str(index)) 
    
    
    
    
    
    
    
