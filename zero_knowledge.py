#!/usr/bin/python

import sys
import random
import time

# How lucky can we actually get for a zero knowledge proof?
# The probability is present. Guessing once is 1/2, twice is 1/4, three is 1/8, etc. but with the speed of a computer
# how high can we reach. A zero-knowledge-proof is used in computation

# Let's say we guess 2 every time, the answer is either 1 or 2. How many right guesses can we get in a row?

max_streak = 0
current_streak = 0

if (len(sys.argv) != 2):
    print ("Usage ./zero_knowledge.py <streak_to_reach>")
else:
    
    i = 0
    streak = int(sys.argv[1])
    while (1):
        random.seed(time.time())
        n = random.randint(1, 2)
        if (n == 2):
            if (current_streak > max_streak):
                max_streak = current_streak
                if (max_streak >= streak):
                    print ("Streak = " + str(max_streak) + ", iterations = " + str(i))
                    break
            current_streak = 0
        else:
            current_streak += 1
        i += 1

"""
    Results:
    Streak = 10, iterations = 52, 2^10 = 1024    
    Streak = 16, iterations = 22523. 2^16 = 65536
    Streak = 20, iterations = 123494, 2^20 = 1048576
    Streak = 25, iterations = 10447756, 2^25 = 33554432   
"""
