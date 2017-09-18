#!/usr/bin/python

# Separates an array into two parts of positive and negative integers
# O(N) and O(1) but doesn't retain original order

import sys

arr = [-12, 1, 2, 4, -3, 5, -8, 0, -14, -22, -30, 3]

count = 0
for i in range(len(arr)):
    if (arr[i] < 0):
    	count += 1

end = len(arr) - 1
for i in range(0, len(arr) - (count - 1)):
	if (arr[i] < 0):
		for j in range(end, len(arr) - count, -1):
			if (arr[j] >= 0):
				arr[i], arr[j] = arr[j], arr[i]
				end = j
				break
				
print arr
