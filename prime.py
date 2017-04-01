#!/usr/bin/python2

import sys

# Okay this was kind of interesting because finding prime without complex algorithms is sqrt(N)
# I searched a bit about other algorithms, very interesting what we do for huge numbers

def prime_calculator (prime):

    initial_divider = 1
    prime_status = 0

    i = 2
    while (prime/i >= i):
        if (prime % i == 0):
            prime_status = 1
            break;
        i = i + 1
        
    if (prime_status == 0):
        print (str(prime) + " prime")
    else:
        print (str(prime) + " is not prime")

    return;

if (len(sys.argv) != 2):
    print "./prime.py <number>"
else:
    prime_calculator(int(sys.argv[1]))


