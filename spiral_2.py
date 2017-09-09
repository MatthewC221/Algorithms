# Leetcode: https://leetcode.com/problems/spiral-matrix-ii/description/
# Very similar to spiral 1, instead of checking for false, check for 0. Also assign values
# instead of appending to return list

class Solution(object):

    def isValid(self, i, j, m, n):
        return ((i >= 0 and i < m) and (j >= 0 and j < n))
    
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if (n == 0):
            return []
        
        matrix = [[0 for x in range(n)] for y in range(n)] 
        
        # Everytime we hit the edge or a -1, swap iterate the direct
        direct = 0
        i = 0
        j = 0
        
        m = len(matrix)
        n = len(matrix[0])
        count = 1
        
        while (count < (n ** 2) + 1):
            matrix[i][j] = count
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

            if (self.isValid(next_x, next_y, m, n) == False or matrix[next_x][next_y] != 0):
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
        
        return matrix
            
                
            
