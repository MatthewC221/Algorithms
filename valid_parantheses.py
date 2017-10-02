# Leetcode: https://leetcode.com/problems/valid-parentheses/description/
# Using a stack, amortized O(1) operations all round.
# Check if there's anything left in the stack at the end

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Use a stack (actually a list but only use pop and insert)
        stk = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                stk.append(s[i])
            else:
                if (len(stk) > 0):
                    cur = stk.pop()
                    if (s[i] == ')' and cur != '('):
                        return False
                    elif (s[i] == '}' and cur != '{'):
                        return False
                    elif (s[i] == ']' and cur != '['):
                        return False
                else:
                    return False
        
        return len(stk) == 0
