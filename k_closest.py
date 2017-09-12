# Leetcode: https://leetcode.com/problems/find-k-closest-elements/description/
# Definitely could use binary search here for the first part, could even be a faster O(n) (early cancel)
# This was pretty rushed though.

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if (not arr): return []
        
        diff = sys.maxint
        ind = 0
        
        # Could use binary search
        for i in range(len(arr)):
            if (abs(arr[i] - x) < diff):
                diff = abs(arr[i] - x)
                ind = i
        
        ret = [arr[ind]]
        
        before = ind - 1
        after = ind + 1
        
        while (k > 1):
            diff_before = sys.maxint
            diff_after = sys.maxint
            
            if (before >= 0):
                diff_before = abs(arr[before] - x)
            if (after < len(arr)):
                diff_after = abs(arr[after] - x)
            
            if (diff_before <= diff_after):
                ret.insert(0, arr[before])
                before -= 1
            else:
                ret.append(arr[after])
                after += 1
                
            k -= 1
            
        return ret
