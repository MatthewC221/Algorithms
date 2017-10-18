# Leetcode: https://leetcode.com/problems/maximum-width-of-binary-tree/description/
# Wow this was pretty difficult.. I was too blindsided by a purely BFS approach I never considered a DFS. 
# Literally beats 0.5%..
# The way I did it was to keep track of distances between nodes, instead of filling up with None.
# For example.

"""
        1
     2    3
   3  N N   4
   
is represented as

        1
     2    3
   3  D1 D1   4
   
If we encounter a distance value we multiply it by 2 (None has 2 none children)
"""
 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS
        
        if (not root): return 0
        
        queue = [root]
        max_size = 1
        new = []
        
        while (len(queue) > 0):
            
            count = 0
            flag = False
            new = []    
            
            # Make the gaps between nodes as an integer, not None nodes
            cnt = 0
            for i in xrange(len(queue)):
                tmp = queue[i]
                if tmp:
                    if isinstance(tmp, int) or isinstance(tmp, long):
                        queue[i] = tmp * 2
                        new.append(tmp * 2)
                    else:
                        # If there's only one number, don't compute max
                        new.append(tmp.left)
                        new.append(tmp.right)
                        if (tmp.left or tmp.right):
                            flag = True
                        cnt += 1 
                else:
                    new.append(1)
            
            if (cnt != 1): max_size = max(max_size, self.evaluate(queue))
            if (flag == False): break
            queue = new

        return max_size

    def evaluate(self, new):
        
        i = 0
        for i in xrange(0, len(new)):
            if (not isinstance(new[i], int) and new[i]): break
        
        j = 0
        for j in xrange(len(new) - 1, -1, -1):
            if (not isinstance(new[j], int) and new[j]): break
        
        if j == i: return 1
        
        dist = 0
        for k in xrange(i, j + 1):
            if isinstance(new[k], int): 
                dist += new[k]
            else: 
                dist += 1
        
        return (dist)
