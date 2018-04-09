# Leetcode: https://leetcode.com/problems/copy-list-with-random-pointer/description/
# One pass, was asked to do it one pass instead of 2 in my Bloom interview. Pretty interesting. 
# The notion of next and random isn't important, just try set everything up as you would, if the next/random node doesn't exist
# CREATE IT!

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodes = {}
        cur = head
        while cur:
            if nodes.get(cur) is None:
                nodes[cur] = RandomListNode(cur.label)
            
            if (nodes.get(cur.next) is None):
                if (cur.next):
                    nodes[cur.next] = RandomListNode(cur.next.label)
                else:
                    nodes[cur.next] = None
            
            if (nodes.get(cur.random) is None):
                if (cur.random):
                    nodes[cur.random] = RandomListNode(cur.random.label)
                else:
                    nodes[cur.random] = None
            
            nodes[cur].next = nodes.get(cur.next)
            nodes[cur].random = nodes.get(cur.random)
            cur = cur.next
        
        return nodes.get(head)
