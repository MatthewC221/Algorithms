# Leetcode: https://leetcode.com/problems/same-tree/description/
# Same tree with BFS iterative, thought it would be faster but it's not really.
# Definitely less elegant and harder to create.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # BFS check
        
        if not p and not q: return True
        
        tree1 = [(p)]
        tree2 = [(q)]
        
        while tree1 or tree2:
            new1 = []
            new2 = []
            if (len(tree1) != len(tree2)): return False
            
            for i in xrange(len(tree1)):
                if ((tree1[i] and tree2[i]) and (tree1[i].val != tree2[i].val)): return False
                if (tree1[i] and not tree2[i] or tree2[i] and not tree1[i]): return False
                if tree1[i]:
                    new1.append(tree1[i].left)
                    new1.append(tree1[i].right)  
                if tree2[i]:
                    new2.append(tree2[i].left)
                    new2.append(tree2[i].right)
                    
            tree1 = new1
            tree2 = new2
        
        return True
        
