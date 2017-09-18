# Leetcode: https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(nlogn), apparently can be done in O(n) with buckets?
        # Not too understanding of the solution right now
        
        freq = [0] * 127
        
        for i in range(len(s)):
            freq[ord(s[i])] += 1
        
        tmp = sorted(range(len(freq)), key=lambda k: freq[k])
        ret = ""
        
        for i in range(len(tmp) -1, -1, -1):
            if (freq[tmp[i]] != 0):
                for j in range(freq[tmp[i]]):
                    ret += chr(tmp[i])
        
        return ret
        
        
