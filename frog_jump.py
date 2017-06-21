# https://leetcode.com/problems/frog-jump/#/description
# TLE on leetcode, I am working on timing issues, it's currently a DFS, BFS was too slow for bigger inputs. 
# I'm quite sure it works.

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
        
        # If not possible
        for i in range(1, len(stones)):
            if (stones[i] - stones[i - 1] > i):
                return False
        
        # While the list is not empty
        while (dp and current_pos < size):
            first = dp.pop(0)
            current_pos = first[0]
            jump_size = first[1]
            
            attempt_jump_position = current_pos + jump_size
            
            # If last stone
            if (attempt_jump_position == stones[len(stones) - 1]):
                return True

            if (attempt_jump_position in stones):    # If there is a stone
                # The three types of jumps!
                standard_jump = ((attempt_jump_position, jump_size))
                if (standard_jump not in dp):
                    dp.insert(0, standard_jump)
                
                larger_jump = ((attempt_jump_position, jump_size + 1))
                if (larger_jump not in dp):
                    dp.insert(0, larger_jump)
                    
                if (jump_size > 1):
                    smaller_jump = ((attempt_jump_position, jump_size - 1)) 
                    if (smaller_jump not in dp):
                        dp.insert(0, smaller_jump)
        
        
        return False
