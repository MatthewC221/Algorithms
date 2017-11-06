# Leetcode: https://leetcode.com/problems/find-the-celebrity/description/
# I remember this from algos, pretty interesting.

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Start everyone as a celebrity
        
        cur = 0
        
        # After this loop only one possible celebrity can remain
        # There are two cases: 
        # If A knows B, eliminate A
        # If A doesn't know B, eliminate B
        
        for i in xrange(1, n):
            if (knows(cur, i) == True): 
                cur = i
        
        # The cur now should be the remaining possible celebrity
        # Testing if everybody knows the celebrity
        for i in xrange(n):
            if (i != cur): 
                if (knows(i, cur) == False): return -1
                if (knows(cur, i) == True): return -1
        
        return cur
        
        
