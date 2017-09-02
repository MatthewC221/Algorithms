# Leetcode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Pretty fast, beats ~88%. It actually tricked me for a while, the thing is you have to 
# get the level by level as normal and append from one side. (Line 39 is the trick)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if (not root):
            return []
        
        queue = [root]
        ret = []   
        flag = True
        
        while (len(queue) > 0):
            
            cur_len = len(queue)
            new = queue[:]
            del queue[:]
            tmp = []
            
            for i in range(cur_len):
                if (new[i].left != None):
                    queue.append(new[i].left)
                if (new[i].right != None):
                    queue.append(new[i].right)
                
                if (flag): 
                    tmp.append(new[i].val)
                else:
                    ind = (i + 1) * -1
                    tmp.append(new[ind].val)
                
            flag = not flag
            ret.append(tmp)
            
        return ret
