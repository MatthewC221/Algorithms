# Leetcode: https://leetcode.com/problems/linked-list-cycle/description/
# I've done this Q before, I took a slight bit of time to figure out when to quit the loop when I realised, the loop 
# will terminate if there is no cycle very early. Otherwise it will slowly catch up to itself!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None: return False
        
        slow = fast = head
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast): return True
        
        return False
