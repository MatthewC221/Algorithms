# Leetcode: https://leetcode.com/problems/target-sum/description/
# Used some help with this, my DP is still pretty weak. Basically like a permutation-style increment
# But adding / subtracting the next element. 

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        if not nums: return 0
        
        first = {}
        if (nums[0] != 0):
            first[nums[0]] = 1
            first[-nums[0]] = 1
        else:
            first[0] = 2
        
        for i in xrange(1, len(nums)):
            nxt = {}
            for tmp in first:
                if (tmp + nums[i] in nxt): 
                    nxt[tmp + nums[i]] += first[tmp]
                else:
                    nxt[tmp + nums[i]] = first[tmp]
                
                if (tmp - nums[i] in nxt): 
                    nxt[tmp - nums[i]] += first[tmp]
                else:
                    nxt[tmp - nums[i]] = first[tmp]
            first = nxt
        
        return first.get(S, 0)
