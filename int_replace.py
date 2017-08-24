# Leetcode: https://leetcode.com/problems/integer-replacement/description/
# This was decent using BFS. However as I saw in the discussion there are many tricks, using bit manip
# and certain patterns, I added the (num + 1) % 4 == 0 part after
# Average: Beats 50%

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BFS for min number
        
        queue = []
        queue.append((n, 0))            # In the form (cur_num, replacements)
        min_replace = None
        
        while (len(queue) > 0):
            (num, replace) = queue.pop(0)
            if (num == 1):               
                min_replace = replace
                break
            elif (num > 1):              # Can't reach solution if num is < 1
                replace += 1
                if (num % 2 == 0):
                    queue.append((num / 2, replace))
                else:
                    if ((num + 1) % 4 == 0 and num > 3):    # Originally I just appended both (num + 1) and (num - 1)
                        queue.append((num + 1, replace))
                    else:
                        queue.append((num - 1, replace))
        
        return min_replace
