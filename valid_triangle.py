# Leetcode: https://leetcode.com/submissions/detail/121185005/
# Beats 99%, check comments below for good explanation

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Triangle numbers are within the bounds a + b > c
        # 3-sum for triangle numbers, bit more complex because you can't just move it. You need to take into consideration other
        # elements.
        # Realise this:
        # [1, 2, 2, 3, 3]
        # [S        E, C]       for start, end, current
        # If S + E > C, that means all elements from S->E can replace S here (ascending)
        # If 1 + 3 > 3, that guarantees 2 + 3 > 3, 2 + 3 > 3, and any other elements
        
        # O(n^2)
        nums.sort()
        count = 0
            
        i = 0
        while (i < len(nums)):
            start = 0
            end = i - 1
            cur = nums[i]
            while (end > start):
                if (nums[start] + nums[end] > cur):
                    count += (end - start)
                    end -= 1
                else:
                    start += 1
            i += 1
        
        return count
