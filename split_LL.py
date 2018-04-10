# Leetcode: https://leetcode.com/problems/split-linked-list-in-parts/description/
# Pretty interesting, weird that you have to count the length yourself tbh.
# Let's do it two passes O(2n) time and O(1) space, you don't need to recreate the nodes as you're only moving forwards

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        count = 0
        cur = root
        while cur:
            count += 1
            cur = cur.next
        
        list_sizes = count / k
        rem = count % k
        sizes = [list_sizes] * k        # Holds when to cut off
        
        for i in xrange(len(sizes)):
            if (rem == 0): 
                break
            sizes[i] += 1
            rem -= 1

        node = root
        ret = []
        for i in xrange(len(sizes)):
            head = cur = None
            for j in xrange(sizes[i]):
                if (j == 0):
                    head = cur = node
                else:
                    cur.next = node
                    cur = node
                node = node.next
            if cur: 
                cur.next = None
            ret.append(head)
        
        return ret
        
