# Not a super hard DP question BUT it was something I thought back to, when I first
# heard it, I had no clue but I realise it was a simple DP. If you could go up to n
# steps at a time, create an array of [1->n]

#!/usr/bin/python

import sys

def upstairs(steps, total):
	
	ways = [0] * (total + 1)
	ways[0] = 1
	for i in range(1, total + 1):
		for j in range(len(steps)):
			if (i >= steps[j]):
				ways[i] += ways[i - steps[j]] 
	
	print ways

if (len(sys.argv) == 2):
	upstairs([1, 2], int(sys.argv[1]))
else:
	print "Usage ./up_stairs.py <steps>"
