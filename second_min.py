# Leetcode: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
# Pretty intuitive solution but slow, the passing of min_val is probably unnecessary. Also the min
# is unnecessary too if we have class objects

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = self.traverse(root, root.val, sys.maxint)
        return (ret if ret != sys.maxint else -1)
    
    def traverse(self, node, min_val, cur):
        
        if (min_val < node.val < cur):
            cur = node.val
            
        if (node.left and node.right):
            return min(self.traverse(node.left, min_val, cur), self.traverse(node.right, min_val, cur))
        
        return cur
