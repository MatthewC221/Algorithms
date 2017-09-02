# Leetcode: https://leetcode.com/problems/number-of-islands/description/
# BFS or DFS each element
# To save speed, maybe use less variables (not sure how else I would)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1"):
                    self.BFS((i, j), grid)
                    count += 1
                    
        return count
        
    def isValid(self, (i, j), m, n):
        return (i >= 0 and i < m) and (j >= 0 and j < n)
    
    def BFS(self, (i, j), grid):
        
        queue = [(i, j)]
        explored = {}
        m = len(grid)
        n = len(grid[0])
        
        while (len(queue) > 0):
            tmp = queue.pop()
            grid[tmp[0]][tmp[1]] = '0'
            explored[(tmp[0], tmp[1])] = 1
            
            left = (tmp[0], tmp[1] - 1)
            right = (tmp[0], tmp[1] + 1)
            top = (tmp[0] + 1, tmp[1])
            bottom = (tmp[0] - 1, tmp[1])
            
            if (self.isValid(left, m, n) and grid[left[0]][left[1]] == "1"
               and left not in explored):
                queue.append(left)
            
            if (self.isValid(right, m, n) and grid[right[0]][right[1]] == "1"
               and right not in explored):
                queue.append(right)
                
            if (self.isValid(top, m, n) and grid[top[0]][top[1]] == "1"
               and top not in explored):
                queue.append(top)
                
            if (self.isValid(bottom, m, n) and grid[bottom[0]][bottom[1]] == "1"
               and bottom not in explored):
                queue.append(bottom)
            
