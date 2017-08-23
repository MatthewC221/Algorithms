# Leetcode: https://leetcode.com/problems/total-hamming-distance/discuss/
# The trick is to compare each bit at the Ith index for each loop. Therefore O(32n)
# My one is slow because I used the binary conversion first when some bit manipulation would do

"""
Bit manip:
ones += (nums[j] >> i) & 1
"""

class Solution(object):
    def totalHammingDistance(self, nums):
        
        # Convert to binary first
        binary = [0] * len(nums)
        for i in range(len(nums)):
            tmp = str(bin(nums[i]))
            tmp = tmp[2:]
            tmp = tmp[::-1]
            binary[i] = tmp
    
        count = 0
        size = len(binary)
        for i in range(32):
            ones = 0
            for j in range(size):
                str1 = binary[j]
                if (len(str1) > i and str1[i] == '1'):
                    ones += 1
            count += ones * (size - ones)

        return count
