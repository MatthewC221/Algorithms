# Leetcode: https://leetcode.com/problems/maximum-swap/description/
# Map out the numbers, e.g. [2, 7, 3, 6] = [-1, -1, 0, 2, -1, -1, 3, 1, -1, -1]
# For each number (e.g. 2 first), search backwards til index 2, if there's an index > 2, swap and ret 

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        num_list = [int(d) for d in str(num)]
        indexes = [-1] * 10
        for i in range(len(num_list)):
            indexes[num_list[i]] = i
        
        ret = 0
        for i in range(len(num_list)):
            for j in range(9, num_list[i], -1):
                if (indexes[j] > i):
                    num_list[indexes[j]], num_list[i] = num_list[i], num_list[indexes[j]]
                    for k in num_list:
                        ret = (ret * 10) + k 
                    return ret
        
        return num
