# Leetcode: https://leetcode.com/problems/binary-tree-right-side-view/description/
# I've done so many of these level by level traversals that it's pretty straight forward now.
# Beats 90%, seems strange for deleting entire objects.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Always return the right most element per level. 
        # Level by level traversal
        
        if not root:
            return []
        
        queue = [(root)]
        ret = []
        
        while (len(queue) > 0):
            copy = queue[:]
            del queue[:]
            
            for i in xrange(len(copy)):
                if (copy[i].left):
                    queue.append(copy[i].left)
                if (copy[i].right):
                    queue.append(copy[i].right)
            
            ret.append(copy[-1].val)
        
        return ret
