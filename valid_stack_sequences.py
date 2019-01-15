# Leetcode: https://leetcode.com/problems/validate-stack-sequences/
# Fan of this solution
# Use the pop array as the main reference for the problem. Since all the elements are unique
# we are forced to pop in the order given.

# E.g [1,2,3,4,5] push -> [4,5,3,2,1] pop
# 4 will need to be popped FIRST:
  # 1. That means before 4 is on the top of the stack only pushes are allowed
  # 2. Nothing can be pushed over 4 as then 4 will never be the first popped element
  
# Next, since 5 has not been seen we will follow the logic of 4 and push until 5 is seen.

# Essentially what the loop [while num not in seen] does is it pushes the number we are looking for to the top of the stack
# If it's already in the stack somewhere we will pop and assume it's at the top position. If not the stack is invalid

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stk = []
        seen = {}
        pushed_ind = 0
        for num in popped:
            while num not in seen:
                cur_push = pushed[pushed_ind]
                stk.append((cur_push))
                seen[cur_push] = True
                pushed_ind += 1
            if num != stk.pop(): return False
            
        return True
