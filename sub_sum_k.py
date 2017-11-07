# Leetcode: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Looks very simple, I like this question a lot. Keep count of the running sum and put in hash each time.
# If running_sum - k exists in hash that means there is a subarray = k. Beats 98%. O(n) time and space

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Keep count of subarray sums
        if not nums: return 0
        
        H = {0:1}
        cnt = 0
        sm = 0
        
        for i in xrange(len(nums)):
            sm += nums[i]
            if (sm-k in H): cnt += H[sm-k]
            
            if (sm in H): H[sm] += 1
            else: H[sm] = 1
        
        return cnt
