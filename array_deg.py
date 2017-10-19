# Leetcode: https://leetcode.com/problems/degree-of-an-array/description/
# Not extremely elegant visually, slow because of the dict iterations
# Still considered O(n) time and O(n) space. A bit awkward with the long k,v pairs

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Find the max frequency in the dict, keep track of its first and last element index
        
        if not nums: return 0
        H = {}
        mx = 1
        
        # Hash values of the form ((start, end), frequency)
        for i in xrange(len(nums)):
            if (nums[i] in H):
                tmp = H.get(nums[i], 0)
                H[nums[i]] = ((tmp[0], i, tmp[2] + 1))
                mx = max(mx, tmp[2] + 1)
            else:
                H[nums[i]] = ((i, -1, 1))
        
        if mx == 1: return 1
        
        min_deg = sys.maxint
        for k, v in H.iteritems():
            if (mx == v[2]): min_deg = min(min_deg, v[1] - v[0] + 1)           # If max element
        
        return min_deg
