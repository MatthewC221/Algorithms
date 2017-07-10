#!/usr/bin/python

import sys
import random 

# First solution to nQueens, only generates single solution
# Starts taking a while around 20.
# Usage ./nQueens.py <number_of_queens>

# Implementation, initialises randomly. Uses least constraint value. If stuck, randomises the board
# Could use simulated annealing to make it faster (will try in future)

# A good design decision would be to compare only with the other Queens, no board necessary

class Solution(object):
    
    def resetPositions(self, Queens, n):

        placed = 0
        while (placed < n):                 # Initialise positions randomly
            col = random.randint(0, n - 1)
            row = random.randint(0, n - 1)
            if ((col, row) not in Queens):
                placed += 1
                Queens.append((col, row))
                
    def getConflicts(self, Queens, row, column, i):

        conflicts = 0

        for counter in range(len(Queens)):
            if (counter != i):
                location = Queens[counter]
                col_diff = abs(location[0] - column)
                row_diff = abs(location[1] - row)
                # If same column, same row, or diagonal
                if (col_diff == 0 or row_diff == 0 or col_diff == row_diff):    
                    conflicts += 1
        
        return conflicts
        
    def printBoard(self, Queens, n):
        
        for i in range(n):
            for j in range(n):
                if ((i, j) not in Queens):
                    sys.stdout.write(" - ")
                else:
                    sys.stdout.write(" Q ")
            print "" 
    
    def solveNQueens(self, n):

        Queens = []     # Holds position of all the queens
        
        self.resetPositions(Queens, n)
        count = 0
        
        while (True):       
            for i in range(len(Queens)):        # Work on one queen at a time
                cur = Queens[i]                 # Current location
                min_constraints = self.getConflicts(Queens, cur[1], cur[0], i)
                
                if (min_constraints):                   # If there is 0 constraints, no better move
                    best_location = (cur[0], cur[1])
                    for col in range(n):                # Go through each available position
                        for row in range(n):
                            if ((col, row) not in Queens):
                                tmp = self.getConflicts(Queens, row, col, i)
                                if (tmp < min_constraints):
                                    best_location = ((col, row))
                                    min_constraints = tmp
                                    
                    Queens[i] = best_location
                    count += 1
                
                total_constraints = 0
                
                for i in range(len(Queens)):
                    total_constraints += self.getConflicts(Queens, Queens[i][1], Queens[i][0], i)
                
                if (total_constraints):                 
                    if (count % n == 0):
                        del Queens[:]
                        self.resetPositions(Queens, n)  
                else:
                    self.printBoard(Queens, n)
                    return

if (len(sys.argv) != 2):
    print "Usage ./nQueens.py <number_Queens>"
else:                
    temp = Solution()
    temp.solveNQueens(int(sys.argv[1]))                            

