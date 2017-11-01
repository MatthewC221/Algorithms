# Leetcode: https://leetcode.com/problems/first-unique-character-in-a-string/description/
# In the midst of exams, this is a leetcode easy. O(n) time and O(n) space

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        for i in xrange(len(s)):
            if (s[i] not in seen): seen[s[i]] = 1
            else: seen[s[i]] += 1
        
        for i in xrange(len(s)):
            if (seen[s[i]] == 1): return i
        
        return -1
