# Leetcode: https://leetcode.com/problems/valid-palindrome-ii/description/
# Beats 70%, could save the function call but this is elegant

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(n)!!!
        # After deleting, create two timelines. One in which we delete the start
        # and one that deletes the end
        # Really surprised the top solution does this exact same thing...
        
        if not s: return True
        
        start = 0
        end = len(s) - 1
        
        while (end > start):
            if (s[start] != s[end]):    # Split the palindrome search into 2
                return self.checkPalindrome(s, start + 1, end) or self.checkPalindrome(s, start, end - 1)
            end -= 1
            start += 1
        
        return True
    
    def checkPalindrome(self, s, start, end):
        
        _start = start
        _end = end
        
        while (_end > _start):
            if (s[_start] != s[_end]): return False
            _end -= 1
            _start += 1
        
        return True
