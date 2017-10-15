# Leetcode: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Very unique idea inspired by a solution, I had a similar idea but didn't fall through

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        h1 = headA
        h2 = headB
        
        if (not h1 or not h2): return None
        
        while (h1 and h2 and h1 != h2):
            h1 = h1.next
            h2 = h2.next
            
            if (h1 == h2):
                return h1
        
            if (not h1): h1 = headB
            if (not h2): h2 = headA
        
        return h1
