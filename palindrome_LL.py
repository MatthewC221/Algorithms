# Leetcode: https://leetcode.com/problems/palindrome-linked-list/description/
# The concept is simple to imagine, however it is a tad annoying because of even/odd length lists.
# The point of the flag, is so if we find the length is odd, we disregard the middle element
# (list is odd if we hit None by doing an ODD number of nexts)

# When in the centre, start popping from stack

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        
        cur = nxt = head
        flag = False
        check = []
        
        while cur:
            if not nxt: flag = True
            if flag == False: 
                nxt = nxt.next
                if nxt: 
                    check.append(cur.val)
                    nxt = nxt.next
            else:
                if (cur.val != check.pop()): return False
            cur = cur.next
        
        return True
