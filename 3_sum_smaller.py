# Leetcode: https://leetcode.com/problems/3sum-smaller/description/
# The trick to 3 sum higher / lower is that once we reach below the target we aren't able to decide to increment
# or decrement start/end.

# However realise this: [-2, 0, 1, 3]
# Let's say we are at indexes 0, 1, 3: [(-2), (0), 1, (3)], because this sum is less than target, we can guarantee
# that if we decrement end however many times our sum will be less than target. That is why we can do: cnt += (end-start)
# O(n^2) + O(nlogn)

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cnt = 0
        print nums
        
        for i in xrange(len(nums)):
            cur = nums[i]
            start = i + 1
            end = len(nums) - 1
            while (start < end):
                if (cur + nums[start] + nums[end] < target): 
                    cnt += (end-start)
                    start += 1
                else:
                    end -= 1
        
        return cnt
