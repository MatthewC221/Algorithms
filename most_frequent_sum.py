# Leetcode: https://leetcode.com/problems/most-frequent-subtree-sum/description/
# O(n^2), beats 5%... my use of the dict is probably poor 
# I see some solutions using post order traversals and such. It could be O(n) but I don't know my
# traversals that well.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root: return []
        freq = {}
        self.traverse(root, freq)
        mx = 0
            
        ret = []
        for k, v in freq.iteritems():
            mx = max(mx, v)
            
        for k, v in freq.iteritems():
            if v == mx:
                ret.append(k)
                
        return ret
        
    def traverse(self, root, freq):
        
        if (root):
            new_val = self.getSubtreeSum(root)
            if (new_val in freq):
                freq[new_val] += 1
            else:
                freq[new_val] = 1
        
        if (root.left):
            self.traverse(root.left, freq)
            
        if (root.right):
            self.traverse(root.right, freq)
            
        return 
    
    def getSubtreeSum(self, root):
        
        if (root.left and root.right):
            return root.val + self.getSubtreeSum(root.left) + self.getSubtreeSum(root.right)
        
        if (root.left):
            return root.val + self.getSubtreeSum(root.left)
        
        if (root.right):
            return root.val + self.getSubtreeSum(root.right)
        
        return root.val
