# Leetcode: https://leetcode.com/problems/4sum-ii/description/
# This was pretty fast, O(n^2) + O(n^2)

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        H = {}
        size = len(A)
        for i in range(size):
            for j in range(size):
                tmp = A[i] + B[j]
                if (tmp in H):
                    H[tmp] += 1
                else:
                    H[tmp] = 1
        
        count = 0
        for i in range(size):
            for j in range(size):
                tmp = (C[i] + D[j]) * -1
                if (tmp in H):
                    count += H[tmp]
        
        return count
        
