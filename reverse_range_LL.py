# Leetcode: https://leetcode.com/problems/reverse-linked-list-ii/description/
# This is a bit tricky because of the edge case when you're reversing the first few elements. You need to change head 
# if that happens. Otherwise consider the reversed part separate and keep track of the before and after.

# E.g. [1, 2, 3, 4, 5], m = 2, n = 4. Keep track of [1,5]. Then 1->head_reversed, tail_reversed->5
# Beats 88%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        # Save the node before and the node after
        
        cur = ret = head
        after = before = None
        cnt = 1
        while cur:
            if (cnt == m - 1):
                before = cur
            elif (cnt == n + 1):
                after = cur
            cnt += 1
            cur = cur.next
        
        # Changing the head (edge case)
        if (before is None):
            H, T = self.reverse(head, (n - m))
            T.next = after
            ret = H
        else:
            H, T = self.reverse(before.next, (n - m))
            before.next = H
            T.next = after
        
        return ret
        
    def reverse(self, node, count, prev=None):
        
        saved = node
        mov = 0
        while (mov < count + 1):
            tmp = node.next
            node.next = prev
            
            prev = node
            node = tmp
            mov += 1
        
        # Prev is the head of the reversed list, saved is the tail of the reversed
        return (prev, saved)
        
