# Leetcode: https://leetcode.com/problems/longest-palindromic-substring/description/
# O(n^2), pretty elegant solution. Was fixed on it being DP for a while but it's quite straight forward.
# Just evaluate the palindrome using the index centre. However even length palindromes need to taken into account. 
# E.g. "ollo"

class Solution(object):
    low = 0
    maxLen = 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (len(s) < 2): return s
        
        # Worst case: O(n^2). 
        # Using the index i as the centre for a possible palindrome
        
        for i in xrange(len(s)):
            self.evaluate(s, i, i)
            self.evaluate(s, i, i + 1)

        return s[self.low-1:self.low+self.maxLen-1]
    
    def evaluate(self, s, start, end):

        while (start >= 0 and end < len(s) and s[start] == s[end]):
            start -= 1
            end += 1
        
        start += 1
        end -= 1
        # Last increment needs to be changed
        
        if (self.maxLen < end - start + 1):
            self.low = start + 1
            self.maxLen = end - start + 1
                
        
