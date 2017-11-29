# Leetcode: https://leetcode.com/problems/asteroid-collision/description/
# Pretty fun question I think. Edge case from line 25-28 to consider. O(n) time and O(n) space using a stack.

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # Positive = travelling right
        # Negative = travelling left
        
        # Use a stack of asteroids going right. Focus on one asteroid at a time.
        
        right = []
        ret = []
        for i in xrange(len(asteroids)):
            if (asteroids[i] > 0): right.append(asteroids[i])
            else:
                if not right: ret.append(asteroids[i])                  # If no asteroid is moving right and some is moving left, it'll survive
                elif (abs(asteroids[i]) == right[-1]):
                    right.pop()
                else:
                    while (right and not abs(asteroids[i]) < right[-1]):    
                        if (abs(asteroids[i]) == right[-1]): 
                            right.pop()
                            break
                        right.pop()
                        if not right: ret.append(asteroids[i])          # Something has destroyed all asteroids moving right
        
        ret.extend(right)
        return ret
