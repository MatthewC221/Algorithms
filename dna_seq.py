# Leetcode: https://leetcode.com/problems/repeated-dna-sequences/description/
# This question is surprisingly straight forward, the trick would be using two dictionaries/hashes.
# However it can still be done with one dict (but only beating 10%).
# O(n)

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        seen = {}                   # Already in our return array
        ret = []
        
        for i in xrange(0, len(s) - 9):
            cur = s[i:i+10]
            if (cur not in first):
                first[cur] = 1
            else:
                if (cur not in seen): 
                    ret.append(cur)
                    seen[cur] = 1
        
        return ret
