# Leetcode: https://leetcode.com/problems/score-after-flipping-matrix/
# I was not super confident that the greedy approach worked, I couldn't think of any other approach so I attempted it this way

# Attempt to flip rows first, then columns. I decided on rows first because flipping a row seemed like an independent action
# I was just trying to maximise the value of my current row. Flipping columns first seemed as if it could punish me later
# if I wanted to flip my rows.

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        # Row flips, if the flipped value is > than original row 
        m, n = len(A), len(A[0])
        for i in xrange(m):
            original = flip = 0 
            for j in xrange(n):
                # Adding the binary representation as we go. E.g. [1,0,0,1] = 2**3 + 0 + 0 + 2**0
                if A[i][j]: 
                    original += 2**(n-j-1)
                else: 
                    flip += 2**(n-j-1)
                    
            if flip > original:
                for j in xrange(n):
                    A[i][j] = int(not A[i][j])
        
        # Column flip, more 0's than 1's makes a flip. (In a column all values have same weighting)
        for j in xrange(n):
            net_effect = 0
            for i in xrange(m):
                if A[i][j]: 
                    net_effect -= 1
                else: 
                    net_effect += 1
            
            if net_effect > 0:
                for i in xrange(m):
                    A[i][j] = int(not A[i][j])
        
        total = 0
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j]: total += 2**(n-j-1)
        
        return total
