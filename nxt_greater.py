# Leetcode: https://leetcode.com/problems/next-greater-element-i/description/
# Beats 80%. I feel like I've done lots of overhead here, with the tuples and the hash assigning
# Definitely could be more elegant but the question itself is strange (could easily been do it for one array).
# O(n) time and O(n) space.

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums: return []

        # Do the question for nums2 then select the indexes after
        # Question meaning: finding the closest greater element on RHS
        stk = [(nums[0], 0)]
        nxt_ind = [-1] * len(nums)
        
        for i in xrange(1, len(nums)):
            while (stk):
                n, ind = stk.pop()
                if (nums[i] < n):
                    stk.append((n, ind))
                    break
                else:
                    nxt_ind[ind] = nums[i]
            stk.append((nums[i], i))
        
        ret = []
        goal = {}
        
        # Organising in the order that the question is requesting (order of findNums)
        for i in xrange(len(nxt_ind)): goal[nums[i]] = nxt_ind[i]
        for i in xrange(len(findNums)):
            ret.append(goal[findNums[i]])
        
        return ret
                    
                    
                
