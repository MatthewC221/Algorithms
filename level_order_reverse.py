# Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
# Done so many level order traversals, reverse it at the end

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        queue = [(root)]
        ret = []
        
        while queue:
            new = []
            lvl = []
            for node in queue:
                if node.left: new.append(node.left)
                if node.right: new.append(node.right)
                lvl.append(node.val)
            
            queue = new
            ret.append(lvl)
        
        return ret[::-1]
                
