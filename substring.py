#!/usr/bin/python

# This is optimised naive, this is not Knuth-morris-pratt

# First argument is the substring

import sys

if (len(sys.argv) == 2):
    substring = sys.argv[1]
else:
    print "./substring.py <substring>"
    sys.exit()

def test_string(location, string_text):

    for i in range(0, len(substring)):
        if (substring[i] != string_text[location+i]):
            return i

    print string_text[location:location+i+1]
    return -1

file = open("string_substring.txt", "r")

string_text = file.read()

in_substring = 0
i = 0

while (i < len(string_text)):
    print string_text[i],
    if (string_text[i] == substring[0]):
        temp = test_string(i, string_text)
        if (temp != -1):
            i = i + temp - 1 
    i += 1
    
    
