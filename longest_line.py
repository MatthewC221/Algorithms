# Leetcode: https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/
# Definitely a bit tricky, especially ondiagonals. You have to increment the rows after the columns has reached the end
# AN example is:
# Beats 90%, O(4n)

"""
By only scanning til the columns you will have seen:

[1, 1, 0, 1]
[1, 0, 0, 0]
[0, 1, 0, 1]

[., ., ., .]
[., ., ., 0]
[., ., 0, 1]

At this point you need to increment the rows
"""

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Scan the entire matrix horizontally, vertically and at each diagonal. (Which is probably the most difficult)
        if not M: return 0
        
        m = len(M)
        n = len(M[0])
        
        streak = 0
        mx = 0
        
        # Scan across
        for i in xrange(m):
            for j in xrange(n):
                if (M[i][j] == 1): 
                    streak += 1
                    mx = max(mx, streak)
                else:
                    streak = 0
            streak = 0
        
        # Scan downwards
        for i in xrange(n):
            for j in xrange(m):
                if (M[j][i] == 1):
                    streak += 1
                    mx = max(mx, streak)
                else:
                    streak = 0
            streak = 0
        
        # Scan anti-diagonally, +1 to row, -1 to col
        # Start from top left
        
        start_cols = 0
        start_rows = 0
        while (start_cols < n and start_rows < m):
            rows = start_rows
            cols = start_cols
            while (rows < len(M) and cols >= 0):
                if (M[rows][cols] == 1):
                    streak += 1
                    mx = max(mx, streak)
                else:
                    streak = 0
                rows += 1
                cols -= 1
            streak = 0
            if (start_cols < n - 1):
                start_cols += 1
            else:
                start_rows += 1
        
        # Scan diagonally, -1 to row, -1 to col
        
        start_cols = 0
        start_rows = m - 1
        while (start_cols < n and start_rows >= 0):
            rows = start_rows
            cols = start_cols
            while (rows >= 0 and cols >= 0):
                if (M[rows][cols] == 1):
                    streak += 1
                    mx = max(mx, streak)
                else:
                    streak = 0
                rows -= 1
                cols -= 1
            streak = 0
            if (start_cols < n - 1):
                start_cols += 1
            else:
                start_rows -= 1
    
        return mx
        
