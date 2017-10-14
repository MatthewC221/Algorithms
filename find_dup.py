# Leetcode: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# This one requires a really smart trick, a flicking of the switch within the array. Subtract 1 from ind
# as to not go over the array.

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Sorting: Time: O(nlogn), Space: N/A
        # Dictionary: Time: O(n), Space: O(n)
        
        ret = []
        for i in xrange(len(nums)):
            ind = abs(nums[i]) - 1
            if (nums[ind] < 0): ret.append(abs(nums[i]))
            nums[ind] *= -1

        return ret
