# Leetcode: https://leetcode.com/problems/out-of-boundary-paths/description/
# TLE, used naive BFS, very close to correct but faster solutions use DP. I'm not entirely sure how I would.

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        # m = rows
        # n = columns
        # N = number of moves
        # i = starting row
        # j = starting col
        
        if (m == 0 or n == 0):
            return 0
        
        count = 0
        queue = []         # Starting positions and moves remaining
        queue.append((i, j, N))
        while (len(queue) > 0):
            tmp = queue.pop()
            
            new = [0] * 4               # Left, up, right, down
            new[0] = ((tmp[0] + 1, tmp[1], tmp[2] - 1))
            new[1] = ((tmp[0] - 1, tmp[1], tmp[2] - 1))
            new[2] = ((tmp[0], tmp[1] + 1, tmp[2] - 1))
            new[3] = ((tmp[0], tmp[1] - 1, tmp[2] - 1))
            
            for i in range(len(new)):
                if (self.isValid(new[i][0], new[i][1], m, n) == False and new[i][2] >= 0):
                    count += 1
                elif (self.isValid(new[i][0], new[i][1], m, n) == True and new[i][2] > 0):
                        queue.append(new[i])
        
        return count
    
    def isValid(self, i, j, m, n):
        
        return (i >= 0 and i < m) and (j >= 0 and j < n)
