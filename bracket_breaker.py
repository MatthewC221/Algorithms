#!/usr/bin/python

import sys
import re

# Bracket breaker prototype, this looks to work. Slowly break down each bracket
# Have my exam to study for... will return to this (TODO)

evaluate = "(5-9)+(6+2)*(6+6)"
m = re.findall('\([0-9]+[+-\/*][0-9]+\)', evaluate, re.MULTILINE)
if (m):
    print m
