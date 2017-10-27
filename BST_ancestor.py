# Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Draw out a tree and find ancestors first. Realise an ancestor is the value between the two nodes.
# Looking for: P <= ANCESTOR <= Q

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # The lowest common ancestor is the first value between two nodes
        while root:
            if ((root.val >= p.val and root.val <= q.val) or 
               (root.val >= q.val and root.val <= p.val)):
                return root
            if (root.val >= p.val and root.val >= q.val):
                root = root.left
            if (root.val < p.val and root.val < q.val):
                root = root.right
        
        return None
