# Leetcode: https://leetcode.com/problems/palindrome-partitioning/description/
# Been on holiday for the past week, I am really weak on backtracking and only recently started doing backtracking questions
# Beats 80%, need to keep extending the palindromes until we reach the end.

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Can check what areas are palindromes, if we can partition from ranges 1->2, 3->4 then it's fine
        all_paths = []
        self.backtrack(s, 0, [], all_paths)
        return all_paths
        
    def backtrack(self, s, start, path, all_paths):
        
        if (start == len(s)):           # If at end of string
            all_paths.append(path[:])
            return
        
        for i in xrange(start, len(s)):
            if (self.isPalindrome(start, i, s)):        # If found a palindrome, find next one at index
                path.append(s[start:i+1])
                self.backtrack(s, i+1, path, all_paths)
                path.pop()                              # This is the backtracking step
    
    def isPalindrome(self, start, end, s):
        
        while (start < end):
            if (s[start] != s[end]): return False
            start += 1
            end -= 1
    
        return True
