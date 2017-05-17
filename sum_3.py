#!/usr/bin/python

import sys
import random

# My friend told me about this question after he received it for a phone interview
# I thought of the solution of sum_2 but with a change.
# What we can do is sort it, and perform sum_2 on the rest of the list

# Question is, find if 3 elements of a list can sum up to a number

def sum_3(Arr, num):

    # Initially sort the list O(nlogn)
    Arr.sort()
    print Arr
    # O(n)
    for i in range(0, len(Arr)):
        starting_sum = Arr[i]
        current = i + 1
        last = len(Arr) - 1
        # O(n)
        while (current < last):
            if (starting_sum + Arr[current] + Arr[last] == num):
                print "The numbers are " + str(starting_sum) + ", " + str(Arr[current]) + ", " + str(Arr[last])
                return True
            elif (starting_sum + Arr[current] + Arr[last] > num):
                last -= 1
            elif (starting_sum + Arr[current] + Arr[last] < num):
                current += 1
    
    # O(n^2) + O(nlogn) = O(n^2)           
    return False

if (len(sys.argv) != 2):
    print "Usage ./sum_3.py <number>"
else:
    arr = []
    for i in range(0, 5):
        arr.append(random.randint(-15, 15))
    
    print (sum_3(arr, int(sys.argv[1])))
        
        
