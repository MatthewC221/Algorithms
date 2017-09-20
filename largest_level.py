# Leetcode: https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Beats 86%, very intuitive and easy to do if you know how to BFS trees level by level

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = [root]
        ret = []
        
        while (len(queue) > 0):
            
            copy = queue[:]
            del queue[:]
            cur = -sys.maxint
            
            for i in xrange(len(copy)):
                cur = max(cur, copy[i].val)
                
                if (copy[i].left): queue.append(copy[i].left)
                if (copy[i].right): queue.append(copy[i].right)
            
            ret.append(cur)
        
        return ret
