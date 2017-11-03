# Leetcode: https://leetcode.com/problems/bomb-enemy/description/
# Pretty straight forward without DP. I think this is the real elegant solution, but the DP is 
# interesting.

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])
        mx = 0
        
        for i in xrange(m):
            for j in xrange(n):
                if (grid[i][j] == '0'): mx = max(mx, self.BFS(grid, i, j))
        
        return mx
    
    def BFS(self, grid, loc_x, loc_y):
        
        # Can do four different loops
        
        # Scanning right
        count = 0
        for i in xrange(loc_y, len(grid[0])):
            if (grid[loc_x][i] == "W"): break
            elif (grid[loc_x][i] == "E"): count += 1
                
        # Scanning left
        for i in xrange(loc_y, -1, -1):
            if (grid[loc_x][i] == "W"): break
            elif (grid[loc_x][i] == "E"): count += 1
        
        # Scanning down
        for i in xrange(loc_x, len(grid)):
            if (grid[i][loc_y] == "W"): break
            elif (grid[i][loc_y] == "E"): count += 1        

        # Scanning up
        for i in xrange(loc_x, -1, -1):
            if (grid[i][loc_y] == "W"): break
            elif (grid[i][loc_y] == "E"): count += 1  
        
        return count
            
            
