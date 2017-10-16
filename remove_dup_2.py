# Leetcode: https://leetcode.com/submissions/detail/123773002/
# This is definitely harder to do, need some extra pointers. I used help to finish the solution off completely because my
# original solution had an edge case. I'd still recommend an elegant approach of two passes. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # One pass, not the easiest thing to think about
        # Better off doing it with two passes and some extra memory for elegance
        
        if not head: return None
        
        cur = head
        newH = ListNode(-1)
        prev = newH
        newH.next = head
        
        while cur:
            while cur.next and cur.val == cur.next.val: cur = cur.next          # Get to the end of the duplicates
            
            if (prev.next == cur): 
                prev = prev.next  
            else: 
                prev.next = cur.next
            cur = cur.next
        
        return newH.next
