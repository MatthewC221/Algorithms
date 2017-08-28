# Leetcode: https://leetcode.com/problems/partition-list/description/
# This was kind of straight forward but my implementation runs very slow, could improve it by pointers
# by the double LL is a good strategy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        if (not head):
            return []
        
        less = None                 # The heads and the cur pointer of the < and >= list
        less_head = None
        more = None
        more_head = None
        
        while (head != None):
            newNode = ListNode(head.val)
            if (head.val < x):
                if (less == None):
                    less = newNode
                    less_head = less
                else:
                    less.next = newNode
                    less = less.next
            else:
                if (more == None):
                    more = newNode
                    more_head = more
                else:
                    more.next = newNode
                    more = more.next
            head = head.next
        
        # If the first list is None, return the second list
        if (less_head == None):
            less_head = more_head
        else:
            less.next = more_head
        
        return less_head
        
