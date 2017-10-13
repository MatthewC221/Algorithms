# Leetcode: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Faster to do BFS in most cases (a DFS can get lucky), level order traversal
# Beats 94%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return 0
        height = 1
        # BFS
        queue = [(root)]
        while queue:
            new = []
            for node in queue:
                if (node.left is None and node.right is None): return height
                if node.left: new.append(node.left)
                if node.right: new.append(node.right)
            queue = new
            height += 1
        
        return height
