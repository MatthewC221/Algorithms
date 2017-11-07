# Leetcode: https://leetcode.com/problems/flatten-2d-vector/description/
# Pretty straight forward although there are edge cases of empty lists. Don't copy the data.

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.cur_ind = 0         # Which vector we are at
        self.lst_ind = 0         # The index at the vector
        
    def next(self):
        """
        :rtype: int
        """
        ret = self.vec[self.cur_ind][self.lst_ind]
        
        if (len(self.vec[self.cur_ind]) - 1 == self.lst_ind):
            self.cur_ind += 1
            self.lst_ind = 0 
        else:
            self.lst_ind += 1

        return ret
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while (self.cur_ind < len(self.vec)):
            if self.vec[self.cur_ind]: break
            self.cur_ind += 1
        
        return (self.cur_ind < len(self.vec))

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
