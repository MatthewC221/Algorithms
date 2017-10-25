# Leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# The best answer for this is using some quick sort method that is guaranteed O(n) and O(1). However it's pretty difficult
# to come up with such a solution.

# The obvious ones are a form of priority queue (arr[] below) or sorting.
# Complexity for queue: Space O(k), Time O(nk) 1 <= k <= n. Sort: Space O(1), Time O(nlogn)

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """  
        arr = [-sys.maxint] * k
        # Largest at end
        # O(nk) time, O(k) space
        # Can sort O(nlogn) but slower
        
        for num in nums:
            self.insertArr(num, arr)
        
        return arr[0]
    
    def insertArr(self, num, arr):
        
        # Attempting to insert num into nums
        
        if (num >= arr[-1]): 
            arr.append(num)
            arr.pop(0)
            return
        
        for i in xrange(len(arr)):
            if (num < arr[i]):
                break
        
        if (i != 0): 
            arr.insert(i, num)
            arr.pop(0)
        
        return
