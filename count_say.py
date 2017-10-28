# Leetcode: https://leetcode.com/problems/count-and-say/description/
# This questions is pretty weird..beats 91%. Don't forget to add the last part of the string
# Refer to line 29

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if (n == 1): return "1"
        if (n == 2): return "11"
        if (n == 3): return "21"
        if (n == 4): return "1211"
        if (n == 5): return "111221"
        
        cur = "111221"
        for i in xrange(5, n):
            nxt = ""
            run_len = 1
            char = cur[0]
            for j in xrange(1, len(cur)):
                if (cur[j] == char): 
                    run_len += 1
                else:
                    nxt += str(run_len) + str(char)
                    run_len = 1
                    char = cur[j]
            nxt += str(run_len) + str(char)
            cur = nxt
        
        return cur
