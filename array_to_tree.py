# Leetcode: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Took me a bit longer than I would've wanted to do this, cropped it at the wrong positions so it repeated forever
# Definitely should draw it out before coding.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
    
        # e.g [0, 1, 2, (3), 4, 5, 6], middle element is root each time
        # [0, (1), 2], [4, (5), 6]
        # [(0)], [(2)], [(4)], [(6)]
        
        return self.convert(None, nums)
    
    def convert(self, root, nums):
        
        if not nums: return None
        middle = len(nums) // 2
        root = TreeNode(nums[middle])

        root.left = self.convert(root.left, nums[:middle])
        root.right = self.convert(root.right, nums[middle+1:])
        
        return root
