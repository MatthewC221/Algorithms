#!/usr/bin/python

import sys
import re

# Bracket breaker prototype, this looks to work. Slowly break down each bracket
# Have my exam to study for... will return to this (TODO)

def evaluate_expression(line):
    
    evaluate = []
    flag = False           
    # If the last digit = 0
    
    # Create the list to evaluate
    temp_str = ""
    
    for i in range(0, len(line)):
        if (line[i].isdigit() or line[i] == '.'):
            temp_str = temp_str + line[i]
            flag = True
        elif (line[i] == '+' or line[i] == '*' or line[i] == '-' or line[i] == '/'):
            evaluate.append(temp_str)
            evaluate.append(line[i])
            flag = False
            temp_str = ""
    
    if (flag):
        evaluate.append(temp_str)
    
    # First run does multiplication and division
    new_num = 0
    replace = False
    i = 0
    
    while (len(evaluate) > i):
        if (evaluate[i] == '/'):
            new_num = float(evaluate[i - 1]) / float(evaluate[i + 1])
            replace = True
        elif (evaluate[i] == '*'):
            new_num = float(evaluate[i - 1]) * float(evaluate[i + 1])
            replace = True
        if (replace):
            del evaluate[i-1:i+2]
            evaluate.insert(i-1, new_num) 
            replace = False
            i = i - 2
        i += 1
    
    # Second run does addition and subtraction
    current = float(evaluate[0])
    addition = False
    
    for i in range(1, len(evaluate)):
        if (evaluate[i] == '+'):
            addition = True
        elif (evaluate[i] == '-'):
            addition = False
        else:
            if (addition):
                current += float(evaluate[i])
            else:
                current -= float(evaluate[i])
                
    return current

print ("Only valid inputs please!")
evaluate = raw_input("Enter an equation: ")
evaluate.replace(" ", "")

while (1):
    m = re.findall('\([0-9+-\/*]+\)', evaluate, re.MULTILINE)
    if (not m):
        break
    for i in range(len(m)):
        num = evaluate_expression(m[i])
        evaluate = evaluate.replace(m[i], str(num))
    
ans = evaluate_expression(evaluate)
print ("Answer = " + str(ans))
    
    
    
    
    
    
    
