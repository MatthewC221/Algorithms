# https://leetcode.com/problems/frog-jump/#/description
# My first hard problem solved on leetcode! The big challenge here is the time limit. By rearranging it
# and doing the biggest jumps first I can solve it. Beats 76.77% (not that bad :))
# Uses DFS

# Quick update: So I tried to make it more optimised and be in a higher %. I replaced the inserts with .append() and replaced the
# .pop(0) with .pop() which are both O(1) amortized and it was actually slower?! This is confusing, as insert(0, X) and
# pop(0) are both O(n).

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = []
        size = max(stones)
        dp.append((0, 1))
        current_pos = 0
        
        for i in range(1, len(stones)):
            if (stones[i] - stones[i - 1] > i):
                return False
                
        while (dp and current_pos < size):
            first = dp.pop(0)
            current_pos = first[0]
            jump_size = first[1]
            
            attempt_jump_position = current_pos + jump_size
            
            if (attempt_jump_position == stones[len(stones) - 1]):
                return True

            if (attempt_jump_position in stones):    # If there is a stone
                
                # Smallest stone is inserted first (therefore will be at index 2 when the large ones come in)
                if (jump_size > 1):
                    smaller_jump = ((attempt_jump_position, jump_size - 1)) 
                    if (smaller_jump not in dp):
                        dp.insert(0, smaller_jump)

                standard_jump = ((attempt_jump_position, jump_size))
                if (standard_jump not in dp):
                    dp.insert(0, standard_jump)
                
                # Do largest jumps first
                larger_jump = ((attempt_jump_position, jump_size + 1))
                if (larger_jump not in dp):
                    dp.insert(0, larger_jump)
        
        
        return False
