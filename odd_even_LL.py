# Leetcode: https://leetcode.com/problems/odd-even-linked-list/description/
# Straight forward, basically separate the list into two

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None): return None
        
        odd = head
        even = head.next
        evenH = even
        
        while (even and even.next):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = evenH
        
        return head
