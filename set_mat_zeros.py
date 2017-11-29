# Leetcode: https://leetcode.com/problems/set-matrix-zeroes/description/
# O(n) time, O(n) space. I think this is a good way to do it, it will never be O(n^2).
# Even if we approached in the manner that if we see a 0 we set its col and row to False we can reach O(n^2).
# This way, we only go through each row/col at most once at the cost of the dict.

# Beats 90%

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # Maintain setting 0 list
        rows = []
        cols = []
        
        rows_seen = {}
        cols_seen = {}
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in xrange(m):
            for j in xrange(n):
                if (matrix[i][j] == 0):
                # Ensure we only set each row/col ONCE
                    if (i not in rows_seen):
                        rows.append(i)
                        rows_seen[i] = 1
                    if (j not in cols_seen):
                        cols.append(j)
                        cols_seen[j] = 1
        
        # Set them all to 0
        for i in xrange(len(rows)):
            for j in xrange(n): matrix[rows[i]][j] = 0
        
        for i in xrange(len(cols)):
            for j in xrange(m): matrix[j][cols[i]] = 0
        
