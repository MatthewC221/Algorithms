# Leetcode: https://leetcode.com/problems/score-of-parentheses/description/
# O(n) time and space, beats 90-100% 
# This feels quit elegant to me, we break things down when brackets close. We insert integers to replace closed brackets
# If we have two integers next to one another, we will add them, e.g. ["(", 1, 2] => ["(", 3]

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # Expand from the () first
        expand = list(S)
        stk = []
        for val in expand:
            if val == "(":
                stk.append(val)
            elif val == ")":
                if stk and stk[-1] == "(":
                    stk.pop()
                    stk.append(1)
                elif len(stk) > 1 and isinstance(stk[-1], int) and stk[-2] == "(":
                    val = stk.pop()
                    stk.pop()
                    stk.append(2*val)
            
            if len(stk) > 1:
                if isinstance(stk[-1], int) and isinstance(stk[-2], int):
                    stk.append(stk.pop() + stk.pop())
                
        return stk[0]
            
