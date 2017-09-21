# Leetcode:
# Max depth of tree, pretty straight-forward
# Beats 70% but fluctuates, for speed use iteration and DFS/BFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """      
        if (not root): return 0
        
        queue = [root]
        height = 0
        while (len(queue) > 0):
            new = []
            while (len(queue) > 0):
                cur = queue.pop()
                if (cur.left):
                    new.append(cur.left)
                if (cur.right):
                    new.append(cur.right)
            
            queue.extend(new)
            height += 1
        
        return height
