# Leetcode: https://leetcode.com/problems/symmetric-tree/description/
# Level order traversal, I've seen some solutions using stack. The small trick here is to maintain the None
# The example they showed, with [1,2,2,null,3,null,3] makes you second guess a level traversal but just append
# null values too. Also be careful of calling node.val on [null] nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Level order traversal will do best (also can do recursively, check left = right)
        
        if not root: return True
        queue = [(root)]
        
        while queue:
            new = []    
            for i in xrange(len(queue)):
                if queue[i] is not None:            # We will store the None (but not actually explore it)
                    new.append(queue[i].left)
                    new.append(queue[i].right)
                
                opp = -1 * (i + 1)
                if queue[i] is None and queue[opp] is not None: return False
                if queue[i] is not None and queue[opp] is None: return False
                
                if (queue[i] and queue[opp]):
                    if (queue[i].val != queue[opp].val): 
                        return False
            
            queue = new
        
        return True
                
                
