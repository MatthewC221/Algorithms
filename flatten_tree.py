# Leetcode: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# This is pretty difficult imo. You want to keep all the right subtrees in the stack, keep
# moving through left subtrees. 

# One way to think about it is, The left children come first. Then the right.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return None
        right_tree = []
        while root:
            while root.left:
                if root.right: right_tree.append(root.right)
                root.right = root.left
                root.left = None
                root = root.right
            if (root and root.right is None and right_tree):
                root.right = right_tree.pop()
            root = root.right
