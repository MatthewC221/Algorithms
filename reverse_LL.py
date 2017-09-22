# Leetcode: https://leetcode.com/problems/reverse-linked-list/description/
# Reverse linked list iterative and recursive, I need to work more with LL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        prev = None
        cur = head
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            
        return prev
        """
        return self.reverse(head)
    
    def reverse(self, cur, prev=None):
        
        if (cur is None):
            return prev 
        
        tmp = cur.next
        cur.next = prev
        
        return self.reverse(tmp, cur)
        
    
