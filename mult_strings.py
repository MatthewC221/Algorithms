# Leetcode: https://leetcode.com/problems/multiply-strings/description/
# O(n^2) multiply strings, takes a little bit of time to figure out exactly what you need to do
# E.g. for the last multiplication keep the whole number (7 * 5 = 35 not 5)

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        mult = 1
        overflow = 0
        tot = 0
        
        for i in range(len(num1) - 1, -1, -1):
            cur = int(num1[i])
            multiplier = 1
            current_number = 0
            overflow = 0
            
            k = len(num2) - 1
            j = 1                           # Avoid single digit multiplications (when calling num2[j-1])
            for j in range(k, 0, -1):    
                num = (cur * int(num2[j])) + overflow
                rem = (num / 10)
                current = num % 10
                current_number += (current * multiplier)
                multiplier *= 10
                overflow = rem
            
            num = (cur * int(num2[j - 1])) + overflow
            current_number += (num * multiplier)
            
            current_number *= mult
            tot += current_number
            mult = mult * 10
                
        return str(tot)
