class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        grid = [[0 for i in range(n)] for j in range(m)]

        # The trouble is with the first column and first row, there are some edge cases
        # Note: [1, 0, 0] should equal to 0.  
    
        # Initialise first row
        for i in range(0, n):
            if (i == 0):
                if (obstacleGrid[0][0] == 1):
                    grid[0][i] = 0
                else:
                    grid[0][i] = 1
            else:
                if (obstacleGrid[0][i] == 1 or grid[0][i - 1] == 0):
                    grid[0][i] = 0
                else:
                    grid[0][i] = 1
        
        # Initialise first column
        for j in range(1, m):
            if (obstacleGrid[j][0] == 1 or grid[j - 1][0] == 0):
                grid[j][0] = 0
            else:
                grid[j][0] = 1            

        # Iterate as usual, if the index is an obstacle set it to 0.
        # Otherwise do the normal sum
        for i in range(1, m):
            for j in range(1, n):
                if (obstacleGrid[i][j] != 1):
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                else:
                    grid[i][j] = 0
        
        return grid[m - 1][n - 1]
                
