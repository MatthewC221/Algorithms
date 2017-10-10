# Leetcode: https://leetcode.com/problems/max-area-of-island/description/
# A rather typical DFS question, save the max area. Only beats 65% but this is elegant and there isn't 
# a faster way to do this (complexity-wise). I think some operations are costly such as the function call to isValid
# Otherwise pop and append are O(1) amortized

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        mx = 0
        for i in xrange(m):
            for j in xrange(n):
                if (grid[i][j] == 1):
                    mx = max(self.DFS(grid, (i, j)), mx)
        
        return mx
    
    def DFS(self, grid, (i, j)):
        
        queue = [(i, j)]
        grid[i][j] = 0
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        
        while queue:
            x, y = queue.pop()
            nxt = [0] * 4
            nxt[0] = (x - 1, y)
            nxt[1] = (x + 1, y)
            nxt[2] = (x, y - 1)
            nxt[3] = (x, y + 1)
            for (i, j) in nxt:
                if (self.isValid((i, j), m, n) == True and grid[i][j] == 1):
                    grid[i][j] = 0
                    queue.append((i, j))
            cnt += 1
        
        return cnt
        
    
    def isValid(self, (i, j), m, n):
        return (i >= 0 and i < m) and (j >= 0 and j < n)
