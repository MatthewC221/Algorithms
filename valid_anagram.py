# Leetcode: https://leetcode.com/problems/valid-anagram/description/
# Can save the additional array space by subtracting instead

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if (len(t) != len(s)): return False
        
        a = [0] * 26
        for i in xrange(len(s)):
            fir = ord(s[i]) - 97
            sec = ord(t[i]) - 97
            a[fir] += 1
            a[sec] -= 1
        
        for i in xrange(len(a)):
            if (a[i] != 0): return False
        
        return True
            
