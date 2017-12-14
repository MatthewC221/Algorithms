# Leetcode: https://leetcode.com/problems/frog-jump/description/
# Beats 99-100%! I redid this question from 5 months ago but I optmised it with some small things that everyone would do,
# I hashed the old jump configs as to not repeat the same thing as well as hashing the stones. This along with DFS
# really boosts the speed.

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        stk = []
        size = max(stones)
        stk.append((0, 1))
        current_pos = 0
        
        seen_jump = {}
        all_stones = {}
        
        for i in range(1, len(stones)):
            if (stones[i] - stones[i - 1] > i):
                return False
            all_stones[stones[i]] = 1
                
        while (stk and current_pos < size):
            first = stk.pop()
            seen_jump[first] = 1
            current_pos, jump_size = first[0], first[1]
            attempt_jump_position = current_pos + jump_size
            
            if (attempt_jump_position == stones[-1]): return True

            if (attempt_jump_position in all_stones):           # If there is a stone to jump to
                if (jump_size > 1):
                    smaller_jump = ((attempt_jump_position, jump_size - 1))             # Attempt a small jump
                    if (smaller_jump not in seen_jump):
                        stk.append(smaller_jump)

                standard_jump = ((attempt_jump_position, jump_size))                    # Attempt a standard jump
                if (standard_jump not in seen_jump):
                    stk.append(standard_jump)
                
                larger_jump = ((attempt_jump_position, jump_size + 1))                  # Attempt a larger jump
                if (larger_jump not in seen_jump):
                    stk.append(larger_jump)
        
        
        return False
