# Leetcode: https://leetcode.com/problems/max-consecutive-ones-iii/
# This solution is kind of strange yet it felt intuitive when I first thought of it. 
# We basically try to extend the window as far as possible, so if there were 3 zeros at index 3, 5 zeros at index 12 and K = 2
# There are only two zeros from index 3->12, therfore we are able to create a window from index 3->12. 

# This doesn't take into account a natural window of 1's occuring before our artificial one. That's why we consider the one's streak

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ones_streak = [0] * len(A)
        zero_indexes = {}
        zero_count = 0
        max_streak = 0
        for i in xrange(len(A)):
            if A[i] == 1:
                if i > 0:
                    ones_streak[i] = ones_streak[i-1] + 1
                    max_streak = max(max_streak, ones_streak[i])      # If K == 0 we need this
                else:
                    ones_streak[i] = 1
            else:
                zero_count += 1
                zero_indexes[zero_count] = i
                
            stretch = zero_count - K + 1
            if stretch in zero_indexes:
                length = 0
                index = zero_indexes[stretch]
                if index > 0: length += ones_streak[index-1]
                max_streak = max(max_streak, length + (i - index + 1))
        
        if K >= zero_count: return len(A)   # An edge case (we only look for optimal stretching), if there is
                                            # no optimal stretch that means we can't physically find a window where there is >= K
                                            # zeros. We can fill the whole list due to this.
        
        return max_streak
