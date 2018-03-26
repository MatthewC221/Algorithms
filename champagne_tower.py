# Leetcode: https://leetcode.com/problems/champagne-tower/description/
# Only uploading this because I like the question a lot.

"""
Set the top glass to the pour count, could be 1000. Doesn't matter. Keep overflowing the cups to the next level IFF
the cup content > 1. Do some small optimizations by exiting if we find the query glass. Remember in reality the glass
is only holding a max of 1.0 pours (even if it's overflowing it will be 1.0)

About time + space:
    - Kinda dynamic programming, can do naively by starting to pour from the top everytime.
    - Time would be O(kn) where k = number of rows to process (max 99) and n = cups in the row
    - Space efficient, only holds two rows at max at one time.
"""

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        
        # Can start at the top each time but too slow.
        # Start the top glass at = poured, split it each time (if > 1)
        row_count = 0
        row_content = [poured]     
        while (1):
            next_row = [0] * (row_count + 2) 
            exit = True
            for i in xrange(len(row_content)):
                if (row_count == query_row and i == query_glass):
                    return 1 if row_content[i] > 1 else row_content[i]
                elif (row_content[i] > 1):       # If overflow
                    overflow = row_content[i] - 1
                    next_row[i] += float(overflow) / 2
                    next_row[i+1] += float(overflow) / 2
                    exit = False
            
            if (exit): break  
            row_content = next_row
            row_count += 1
        
        return 0.0
