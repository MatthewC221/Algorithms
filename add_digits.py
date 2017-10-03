# Leetcode: https://leetcode.com/problems/add-digits/description/
# Didn't do the O(1) version, but this runs fast too. Had beats 99% and then 55%
# Not sure why it can be so inconsistent

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        s = 0
        while num > 9:
            while num:
                s += num % 10
                num //= 10
            num = s
            s = 0
            
        return num
