# Leetcode: https://leetcode.com/problems/dungeon-game/description/
# This was difficult, I tried ordinary dp, dfs and then did some more thinking, it requires
# a different form of DP in which you're saying the min health of the path

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # Dynamic programming
        starting_HP = 0
        
        # Make 2D dp array
        size_x = len(dungeon[0])
        size_y = len(dungeon)        
        
        dp = [[99999 for x in range(size_x + 1)] for y in range(size_y + 1)] 
        dp[size_y - 1][size_x] = 1
        dp[size_y][size_x - 1] = 1
        
        """
        Initial DP solution...
        
        dp[0][0] = dungeon[0][0]
        # Initialise 
        for i in range(1, size_y):
            dp[i][0] = dp[i - 1][0] + dungeon[i][0]
        
        for j in range(1, size_x):
            dp[0][j] = dp[0][j - 1] + dungeon[0][j]
        
        for i in range(1, size_y):
            for j in range(1, size_x):
                effect = dungeon[i][j]
                dp[i][j] = max(dp[i - 1][j] + effect, dp[i][j - 1] + effect
        """
        
        
        for i in range(size_y - 1, -1, -1):
            for j in range(size_x - 1, -1, -1):
                tmp = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                if (tmp <= 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = tmp
        
        # min_val = self.dfs(dungeon, size_x, size_y)
              
        return dp[0][0]
    """
    DFS that I didn't end up using, even with backtracking it's not fast enough
    
    def dfs(self, dungeon, size_x, size_y):
        
        queue = []
        queue.append((dungeon[0][0], (0, 0), dungeon[0][0]))  # Maintain the current health, cur xy and min of trip
        total_max = -9999
        
        while (len(queue) > 0):
            cur_HP, pos, min_val = queue.pop()
            y = pos[0]
            x = pos[1]
            if (y == size_y - 1 and x == size_x - 1):
                total_max = max(total_max, min_val)
            else:
                if (pos[0] < size_y - 1):
                    new_HP = cur_HP + dungeon[y + 1][x]
                    new_min = min(min_val, new_HP)
                    if (new_min > total_max):
                        queue.append((new_HP, (y + 1, x), new_min))
                    
                if (pos[1] < size_x - 1):
                    new_HP = cur_HP + dungeon[y][x + 1]
                    new_min = min(min_val, new_HP)
                    if (new_min > total_max):
                        queue.append((new_HP, (y, x + 1), new_min))
        
        if (total_max < 0):
            return (total_max * -1) + 1
        else:
            return 1
    """
