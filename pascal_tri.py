# Leetcode: https://leetcode.com/problems/pascals-triangle/description/
# Not sure if this is really DP, because it seems like the only way to calculate it.
# Beats 83%, not sure how you would speed it up. 

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # DP using the last array index
        if numRows == 0: return []
        
        # Each row element is a[row][x] == a[row-1][x] + a[row-1][x-1]
        ret = [[1]]
        for i in xrange(1, numRows):
            nxt = [1] * (i + 1)             
            for j in xrange(1, i):                      # The first and last index = 1
                nxt[j] = ret[-1][j] + ret[-1][j - 1]    # do not calculate
            ret.append(nxt)
        
        return ret
