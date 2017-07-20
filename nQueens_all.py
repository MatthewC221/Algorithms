#!/usr/bin/python

import sys
import random 

# Usage ./nQueens.py <number_of_queens>

# To get all solutions, make the first queen go down a column
# Did get lots of help for this, more of an exercise to understand code and translate efficiently

class Solution(object):

    def __init__(self, n):
    
        self.starting_row = 0
        self.starting_col = 0
        self.size = n
        self.board = [[0 for x in range(n)] for y in range(n)] 
                    
    def safe (self, row, col):

        # Check row, column and diagonal
        
        for i in range(0, self.size):
            for j in range(0, self.size):
                if (self.board[i][j]):
                    row_diff = abs(row - i)
                    col_diff = abs(col - j)
                    if (row_diff == 0 or col_diff == 0 or col_diff == row_diff):
                        return False
        
        return True
        
    def printBoard(self):
        
        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i][j]):
                    sys.stdout.write(" Q ")
                else:
                    sys.stdout.write(" - ")
            print ""
        
        print "" 
    
    def resetBoard(self):
        
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = 0
    
    # Back tracking method, follow through a path and go back when failed
    def solveNQueens(self, col):
        
        if (col == self.size):
            self.printBoard()
            return 
        
        for i in range(0, self.size):
            if (self.safe(i, col)):
                self.board[i][col] = 1
                
                self.solveNQueens(col + 1)
                
                # If it reaches this point we have to go back a step
                self.board[i][col] = 0
        
        return 
            
if (len(sys.argv) != 2):
    print "Usage ./nQueens.py <number_Queens>"
else:                
    temp = Solution(int(sys.argv[1]))
    temp.solveNQueens(0)                            

