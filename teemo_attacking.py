# Leetcode: https://leetcode.com/problems/teemo-attacking/description/
# Beats 91%, pretty straight forward O(n) solution. Lots of dislikes probably from the description
# Just check overlap with the former time. Multiple overlaps are taken care of by looking at each
# individual overlap

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # Check overlaps of the previous element
        
        if not timeSeries:
            return 0
        
        count = duration      
        for i in xrange(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i - 1]
            if (diff < duration):
                count += (duration - (duration - diff))
            else:
                count += duration
        
        return count
