# Leetcode: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# Basically can use a hash/set to track numbers, too slow if two-sum downwards for each node
# Dict is faster, beats 90% with dict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        # Top down
        if not root:
            return False
        
        queue = [root]
        nums = set()
        # nums = {}
        
        while (len(queue) > 0):
            tmp = queue.pop()
            if (k - tmp.val in nums):
                return True
            
            nums.add(tmp.val)
            # nums[tmp.val] = 1
            if (tmp.left):
                queue.append(tmp.left)
            if (tmp.right):
                queue.append(tmp.right)
        
        return False
