# Leetcode: https://leetcode.com/problems/add-two-numbers-ii/description/
# Really slow, beats 20%. This requires 3 reverses and another iteration through both lists = O(4n)
# Also the reverse is recursive which slows down speed even more. Use a stack or something for really good speeds

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (not l1 and not l2): return None
        
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        new = None
        ret = None
        
        overflow = 0
        while (l1 or l2):
            cur = overflow
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            
            if (cur > 9): 
                cur -= 10
                overflow = 1
            else:
                overflow = 0
            
            newNode = ListNode(cur)
            if (new == None):
                new = newNode
                ret = new
            else:
                new.next = newNode
                new = newNode
                            
        if (overflow == 1):
            new.next = ListNode(1)
        
        return self.reverse(ret)
        
    def reverse(self, cur, prev=None):
        
        if (cur is None):
            return prev 
        
        tmp = cur.next
        cur.next = prev
        
        return self.reverse(tmp, cur)
