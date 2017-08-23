# Leetcode: https://leetcode.com/problems/4sum/discuss/
# Not the best solution at all, O(n^3) but easy to understand and straight forward to create

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(nums)
        ret = []
        H = {}
        for i in range(size):
            H[nums[i]] = i
                       
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if (target - (nums[i] + nums[j] + nums[k]) in H):
                        val = H[target - (nums[i] + nums[j] + nums[k])]
                        if (val != i and val != j and val != k):
                            tmp = []
                            tmp.append(nums[i])
                            tmp.append(nums[j])
                            tmp.append(nums[k])
                            tmp.append(nums[val])
                            tmp.sort()
                            if (tmp not in ret):
                                ret.append(tmp)
                        
        return ret
                        
