# Leetcode: https://leetcode.com/problems/license-key-formatting/description/
# Some of these questions are hella weird to be honest. Quite straight forward, be careful of edge cases.
# Realise there's an elegant way to find out the length of the first group. If you have 8 chars and groups of 3, your first group
# is length 2. That's why start = len(S) % K makes sense.

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper()
        S = S.replace('-', '')
        
        ret = ""
        start = len(S)%K
        if (start != 0):
            for i in xrange(0, start): 
                ret += S[i]
            if (i != len(S)-1): ret += "-"
        
        count = 0
        for i in xrange(start, len(S)):
            if (count%K == 0 and count != 0): ret += "-"
            ret += S[i]
            count += 1
        
        return ret
