# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://leetcode.com/problems/construct-string-from-binary-tree/#/description
class Solution(object):
    
    empty_string = ""
    
    def tree2str(self, t):
        
        self.createString(t)
        return self.empty_string
            
    def createString(self, t):
        if (t == None):
            return
        
        self.empty_string = self.empty_string + str(t.val)
        if (t.left == None and t.right == None):
            return 
        
        # If right is not none, we have to print left regardless of if it's null
        if (t.right != None):
            self.empty_string = self.empty_string + "("
            self.tree2str(t.left)
            self.empty_string = self.empty_string + ")"
            self.empty_string = self.empty_string + "("
            self.tree2str(t.right)
            self.empty_string = self.empty_string + ")"
  
        elif (t.left != None):
            self.empty_string = self.empty_string + "("
            self.tree2str(t.left)
            self.empty_string = self.empty_string + ")"

