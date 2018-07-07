# Leetcode: https://leetcode.com/problems/making-a-large-island/description/
# Beats 96-99% on LC, I like this concept. The tricky part to this question is the fact that you need to differentiate islands
# You can not join an area of 3 island to itself (apparent when doing the q)

# The three steps I used were:
"""
1. BFS to calculate total area of every island
2. Set area of island to every element in island NOTING the origin of BFS or the island number
3. Check every 0 to connect 4 possible adjacent islands

The trick is in step 2, to make every island unique I used the origin of step 1's BFS. A better solution (memory wise)
is just to count number of islands and set the island number
"""

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Set the area of an island after propogating through
        # Look for an intersection between two islands, be careful of the same island connecting. 
        
        # Use the code of origin (where we started the BFS from), e.g. [0, 0, 3]
        # E.g. 
        """
        0 0 4 1 4
        0 0 4 0 0
        0 0 I 0 0
        0 0 3 3 3
        0 0 0 0 0
        """
        m = len(grid)
        n = len(grid[0])
        
        area = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(self.bfs(i, j, grid), area)
        
        mx = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 0:
                    nxt = [(i+1, j),(i-1, j),(i, j+1),(i,j-1)]
                    combined_area = 1
                    uniq_islands = {}
                    for nxt_x, nxt_y in nxt:
                        if self.isValid(nxt_x, nxt_y, m, n):
                            # If not list, adjacent grid value is 0
                            if isinstance(grid[nxt_x][nxt_y], list):
                                origin_x, origin_y = grid[nxt_x][nxt_y][0], grid[nxt_x][nxt_y][1]
                                if (origin_x, origin_y) not in uniq_islands:
                                    uniq_islands[(origin_x, origin_y)] = grid[nxt_x][nxt_y][2]

                    for origin, area in uniq_islands.iteritems():
                        combined_area += area
                    mx = max(mx, combined_area)
        
        return mx if mx != 0 else area
        
    # Calculate area and then set it 
    def bfs(self, i, j, grid):
        m = len(grid)
        n = len(grid[0])
        
        visited = {}
        stk = [(i, j)]
        to_set = []
        area = 0
        
        while stk:
            x, y = stk.pop()
            if (x, y) in visited:
                continue
            visited[(x, y)] = 1
            to_set.append((x, y))
            nxt = [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]
            
            for nxt_x, nxt_y in nxt:
                if (nxt_x, nxt_y) not in visited and self.isValid(nxt_x, nxt_y, m, n) and grid[nxt_x][nxt_y] == 1:
                    stk.append((nxt_x, nxt_y))
            area += 1
        
        # Backtrack through to set every index of island = area
        for loc in to_set:
            x, y = loc[0], loc[1]
            grid[x][y] = [i, j, area]
        
        return area
        
    def isValid(self, x, y, m, n):
        return x >= 0 and x < m and y >= 0 and y < n
        
        
