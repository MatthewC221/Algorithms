# Leetcode easy: https://leetcode.com/problems/maximum-product-of-three-numbers/#/description
# Slightly tricky unless you realise line 10.

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Max = max of top three numbers or top number and smallest negative numbers
        # O(N)
        
        min_arr = [1001] * 2
        max_arr = [-1001] * 3
        
        for i in range(len(nums)):
            if (nums[i] < min_arr[0]):
                min_arr[1] = min_arr[0]
                min_arr[0] = nums[i]
            elif (nums[i] < min_arr[1]):
                min_arr[1] = nums[i]
                
            if (nums[i] > max_arr[0]):
                max_arr[2] = max_arr[1]
                max_arr[1] = max_arr[0]
                max_arr[0] = nums[i]  
            elif (nums[i] > max_arr[1]):
                max_arr[2] = max_arr[1]
                max_arr[1] = nums[i]
            elif (nums[i] > max_arr[2]):
                max_arr[2] = nums[i]
        
        return (max(max_arr[0] * max_arr[1] * max_arr[2], 
                    max_arr[0] * min_arr[1] * min_arr[0]))

        """ 
        Using heapq much faster
        
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Max = max of top three numbers or top number and smallest negative numbers
        
        max_arr = heapq.nlargest(3, nums)
        min_arr = heapq.nsmallest(2, nums)
        
        return (max(max_arr[0] * max_arr[1] * max_arr[2],
                   min_arr[0] * min_arr[1] * max_arr[0]))
        
        """
