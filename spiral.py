# Leetcode: https://leetcode.com/problems/spiral-matrix/description/
# This actually took way longer than expected, I made a lot of silly errors, I keep forgetting Python is [row][col]
# Relatively fast but defs better way of doing it, beats 70%

class Solution(object):
    
    def isValid(self, i, j, m, n):
        return ((i >= 0 and i < m) and (j >= 0 and j < n))
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (not matrix):
            return []
        elif (len(matrix) == 1):
            return matrix[0]
        
        # Everytime we hit the edge or a -1, swap iterate the direct
        direct = 0
        i = 0
        j = 0
        
        m = len(matrix)
        n = len(matrix[0])
        ret = [0] * (m * n)
        count = 0
        
        while (count < (m * n)):
            ret[count] = matrix[i][j]
            matrix[i][j] = False
            next_x = i
            next_y = j
            
            if (direct == 0):       # Right
                next_y = j + 1
            elif (direct == 1):     # Down
                next_x = i + 1
            elif (direct == 2):     # Left
                next_y = j - 1
            elif (direct == 3):     # Up
                next_x = i - 1

            if (self.isValid(next_x, next_y, m, n) == False or matrix[next_x][next_y] == False):
                direct += 1
                if (direct == 4):
                    direct = 0
                    
            if (direct == 0):       # Right
                j += 1
            elif (direct == 1):     # Down
                i += 1
            elif (direct == 2):     # Left
                j -= 1
            elif (direct == 3):     # Up
                i -= 1

            count += 1
            if (count == (m * n)): break
        
        return ret
            
                
            
