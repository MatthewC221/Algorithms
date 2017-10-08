# Leetcode: https://leetcode.com/problems/add-one-row-to-tree/description/
# This question is really weird, beats 65%, not elegant at all.
# There is a trick to it and that is, the next level should be split into [left, None], [None, right] regardless

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        
        # Save the children of the new layer 
        
        if not root: return None
        
        if (d == 1): 
            head = TreeNode(v)
            head.left = root
            head.right = None
            return head
        
        queue = [(root)]
        lvl = 1
        
        while queue:
            new = []
            if (lvl == d - 1):        
                nxt = []                            # The saved next level
                new_lvl = []                        # The inserted level
                for i in xrange(len(queue)):        
                    lft = [None, None]
                    right = [None, None]
                    if (queue[i].left):
                        lft[0] = queue[i].left
                    if (queue[i].right):
                        right[1] = queue[i].right
                    nxt.append(lft)
                    nxt.append(right)
                    queue[i].left = TreeNode(v)
                    queue[i].right = TreeNode(v)
                    new_lvl.append(queue[i].left)
                    new_lvl.append(queue[i].right)
                
                for i in xrange(len(new_lvl)):      # Make new level point to saved next level
                    new_lvl[i].left = nxt[i][0]
                    new_lvl[i].right = nxt[i][1]
                break
                    
            for i in xrange(len(queue)):
                if (queue[i].left):
                    new.append(queue[i].left)
                if (queue[i].right):
                    new.append(queue[i].right)
            queue = new
            lvl += 1
        
        return root
