# Leetcode: https://leetcode.com/problems/maximum-binary-tree/description/
# Very similar to sorted array to tree but using max instead of middle element
# Beats 85%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(None, nums)
        
    def constructTree(self, root, nums):
        
        if not nums: return None
        
        mx = max(nums)
        ind = nums.index(mx)
        
        left = nums[:ind]
        right = nums[ind+1:]
        root = TreeNode(mx)
        
        root.left = self.constructTree(root.left, left)
        root.right = self.constructTree(root.right, right)
        
        return root
        
        
