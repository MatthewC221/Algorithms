# Leetcode: https://leetcode.com/problems/pour-water/
# This was actually slightly tricky, think about it before hand as the edge cases are annoying.
# if (heights[i] < fall_height) is the important part, to constantly check whether the droplet can continue falling.
# O(n^2) time but question is less about complexity and more about solving

class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        
        """
        Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

        If the droplet would eventually fall by moving left, then move left.
        Otherwise, if the droplet would eventually fall by moving right, then move right.
        Otherwise, rise at it's current position.
        """
        
        # Check if can fall on LHS, then RHS, then drop on centre
        # V = water, K = index of drop
        
        while (V > 0):
            filled = False
            # If the water level is above the current level, exit loop
            # Check left 
            if (K - 1 >= 0):
                i = K - 1
                saved = -1
                fall_height = heights[K]
                # If the height isn't descending or staying the same exit
                while (i >= 0 and heights[i] <= heights[i+1]):
                    if (heights[i] < fall_height):              # Let the droplet fall until it can no longer
                        filled = True
                        saved = i
                        fall_height = heights[i]
                    i -= 1
                
                if (filled == True):
                    heights[saved] += 1
            
            # Check right
            if (K + 1 <= len(heights) - 1 and filled == False):
                i = K + 1
                saved = -1
                fall_height = heights[K]
                while (i < len(heights) and heights[i] <= heights[i-1]):
                    if (heights[i] < fall_height):
                        filled = True
                        saved = i
                        fall_height = heights[i]
                    i += 1
                
                if (filled == True):
                    heights[saved] += 1
             
            # Fill current otherwise
            if (filled == False):
                heights[K] += 1
            
            V -= 1
            
        return heights
            
        
        
