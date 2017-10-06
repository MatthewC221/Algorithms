# Leetcode: https://leetcode.com/problems/target-sum/description/
# Because I used some help for the first, I tried reimplementing with an array
# Beats 75%, I feel like DFS could work too.

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        if not nums: return 0
        
        n = sum(nums)
        arr = [0] * (n * 2 + 1)        # Make the array first (0 will be near the middle, goes from -sum to sum)
        
        arr[nums[0] + n] = 1
        arr[-nums[0] + n] += 1
        
        for i in xrange(1, len(nums)):
            nxt = [0] * (n * 2 + 1)
            for j in xrange(len(arr)):
                if (arr[j] != 0):
                    nxt[j + nums[i]] += arr[j]
                    nxt[j - nums[i]] += arr[j]  
            arr = nxt
        
        return arr[n + S] if (n + S) < len(arr) else 0
        
        
