# Leetcode: https://leetcode.com/problems/convert-bst-to-greater-tree/description/
# So many level traversals have been done, this has a bit of a trick but that's about it

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return None
        
        queue = [(root)]
        
        saved = root.val
        while queue:
            new = []
            saved = queue[0].val
            for node in queue:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            queue = new
        
        return saved
