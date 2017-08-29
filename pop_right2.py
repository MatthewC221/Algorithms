# Leetcode: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
# So apparently this one doesn't have a run button, I'm surprised I got it on the first go, beats 93%!
# The deleting seems slow

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        if (not root):
            return
    
        queue = []
        queue.append(root)
        
        while (len(queue) > 0):
            
            nodes = queue[:]
            del queue[:]
            
            for cur in nodes:
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
            
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            
            nodes[len(nodes) - 1].next = None
            
