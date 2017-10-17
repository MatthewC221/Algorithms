# Leetcode: https://leetcode.com/problems/rotate-list/description/
# Can definitely see why people don't like this question, requires breaking down the size if it's greater than length
# You can't keep looping through the LL like: [if (cur is None): cur = head] because you'll TLE
# Not particuarly difficult itself (edge cases annoying)

# How to solve: set one pointer k places infront of other. This will give you the connection area
# Such as [1,2,3,4,5], k=2. newTail will be 3, newHead will be 4, oldTail will be 5.
# newTail.next = None (3->None), oldTail.next=head (4->1), return newHead (5)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # Count (size - k) times, and set that to be the new head. Point to the current
        
        if not head: return None
        if k == 0: return head
        
        saved = newTail = connect = newHead = head
        
        cnt = 0
        tmp = head
        while tmp:                              # This is annoying, get the length first. I TLE'd on [1,2,3]  200000000
            cnt += 1
            tmp = tmp.next
        
        k = k % cnt                             # Reduce k to a range between the size
        if k == 0: return head
        
        cnt = 0
        while k > cnt:
            connect = connect.next   
            cnt += 1
        
        while connect.next:
            newTail = newTail.next
            connect = connect.next
        
        newHead = newTail.next
        newTail.next = None
        connect.next = saved
        
        return newHead
        
