# Leetcode: https://leetcode.com/problems/summary-ranges/description/
# This is slightly annoying because of the string conversion part
# I feel like my solutions are slow because I include too much unnecessary stuff
# E.g. I could make the string part straight away w/o extra loop

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if (not nums):
            return []
        
        ret = []
        ret.append([nums[0]])
        
        for i in range(1, len(nums)):
            new = []
            tmp = nums[i]
            if (tmp > ret[-1][-1] + 1):     # If disconnect from the last element
                ret.append([tmp])
            else:
                if (len(ret[-1]) == 1):
                    ret[-1].append(tmp)
                else:
                    ret[-1][-1] = tmp
        
        str_ret = []
        for i in range(len(ret)):
            cur = ""
            for j in range(0, len(ret[i]) - 1):
                cur += str(ret[i][j]) + "->"
            cur += str(ret[i][-1])
            str_ret.append(cur)
        
        # print ret
        return str_ret
                    
            
