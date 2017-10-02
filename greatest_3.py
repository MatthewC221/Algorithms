# Leetcode: https://leetcode.com/problems/third-maximum-number/description/
# .pop() and .append() are O(1) operations, we want to use these to our advantage.
# Everytime we place something in we perform an O(3) to insert.

class Solution(object):
    def thirdMax(self, nums):
        
        mx = [float('-inf'), float('-inf'), float('-inf')]
        
        # Largest, second largest, third largest format
        
        for num in nums:
            if num not in mx:       # O(n) operation as well
                if num > mx[0]:   
                    mx.insert(0, num)
                    mx.pop()
                elif num > mx[1]: 
                    mx.insert(1, num)
                    mx.pop()
                elif num > mx[2]: 
                    mx.insert(2, num)
                    mx.pop()

        return max(nums) if float('-inf') in mx else mx[2]
            
