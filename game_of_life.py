# Leetcode: https://leetcode.com/problems/game-of-life/description/
# The tricky part is in place, set it to a number that you would later change. You could also add it to a list
# and after go through the list and change it. Beats 70%, could be faster using the above 

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # 4 situations
        # If alive and still alive, leave it
        # If dead and still dead, leave it
        # If alive and dying, set it to -1
        # If dead and becoming alive, set it to -2
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                k = self.getNeighbours(board, i, j)
                if (board[i][j] == 1):
                    if (k < 2 or k > 3):
                        board[i][j] = -1
                else:
                    if (k == 3):
                        board[i][j] = -2
                
        for i in range(m):
            for j in range(n):
                if (board[i][j] == -1):
                    board[i][j] = 0
                elif (board[i][j] == -2):
                    board[i][j] = 1
                
    def getNeighbours(self, board, i, j):
        
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (self.isValid(board, x, y) and (x != i or y != j) and (board[x][y] == 1 or board[x][y] == -1)):
                    count += 1
        
        return count
        
    def isValid(self, board, i, j):
        return (i >= 0 and i < len(board)) and (j >= 0 and j < len(board[0]))
