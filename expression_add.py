# Leetcode: https://leetcode.com/problems/expression-add-operators/description/
# Difficult question, I thought it was 1 digit at first but this is a decent way to do it

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        ret = []
        if (not num): return ret
        self.traverse(ret, "", num, target, 0, 0, 0)
        return ret
    
    def traverse(self, ret, path, num, target, pos, cur, last):
        if (pos == len(num)):
            if (target == cur):
                ret.append(path)
            return
        
        for i in xrange(pos, len(num)):
            if (i != pos and num[pos] == '0'): break
            new = int(num[pos:i+1])
            
            if (pos == 0):
                self.traverse(ret, path+str(new), num, target, i+1, new, new)
            else:
                add_path = path + "+" + str(new)
                minus_path = path + "-" + str(new)
                mult_path = path + "*" + str(new)
                self.traverse(ret, add_path, num, target, i+1, cur+new, new)
                self.traverse(ret, minus_path, num, target, i+1, cur-new, -1 * new)
                self.traverse(ret, mult_path, num, target, i+1, cur-last+last*new, last*new)
        
