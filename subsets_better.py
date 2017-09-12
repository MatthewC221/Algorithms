# Leetcode: https://leetcode.com/problems/subsets/description/
# Subsets of distinct elements. Very elegant, almost O(n^2)

# Example, data: {1, 2, 3}
# First loop:  ret = [[], [1]]
# Second loop: ret = [[], [1], [2], [1, 2]]
# Third loop:  ret = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # If the elements aren't distinct, to get rid of dups do:
        # nums.sort()
        
        ret = [[]]
        for i in range(len(nums)):
            for j in range(len(ret)):
                ret.append(ret[j] + [nums[i]])
                
        return ret
