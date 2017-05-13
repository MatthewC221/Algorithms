#!/usr/bin/python

# Making change problem, n denominations of coins of values 1 = v1 < v2 < v3 < ... vN
# Goal: make change for amount C, using as few coins as possible
# Practicising DP

import sys
import random 
import time

# Find minimum coins for 1...total
def min_coins(coins, total):

    min_arr = [100] * (total + 1)           # Min array
    min_arr[0] = 0                          # 0 coins for 0 dollars

    for curr in range(1, total + 1):
        for j in range(0, len(coins)):
            if (coins[j] <= curr):
                if (min_arr[(curr - coins[j])] + 1 <= curr):
                    min_arr[curr] = min(min_arr[curr], min_arr[(curr - coins[j])] + 1)
                    # If coins are 1, 3, 5 and value = 14
                    # At min[10], we can either be min[7] + 1, min[5] + 5 or min[9] + 1
    
    print "The least amount of coins = " + str(min_arr[total])
    print min_arr


if (len(sys.argv) != 2):
    print ("Usage ./making_change.py <money_amount>")
else:
    coins = []
    coins.append(1)
    
    lower_bound = 2
    upper_bound = 5
    for i in range(0, 2):
        coins.append(random.randint(lower_bound, upper_bound))
        lower_bound += 4
        upper_bound += 4
    
    print ("The coins are: ")
    print coins
    
    min_coins(coins, int(sys.argv[1]))


