# Leetcode: https://leetcode.com/problems/merge-k-sorted-lists/description/
# Beast 75%! My first solution TLE'd. Was O(n^2). 
# This solution should be O(mn) where n = number of elements and m = number of lists!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # Could insert each element one by one O(n^2)
        
        # Idea: start from the beginning of each list. Find the minimum, if its the min
        # Make this list increment, find next.      
        
        ptrs = [None] * len(lists)                       # Pointer array (holds the head of each list)
        PQ = []
        for i in xrange(len(lists)):
            ptrs[i] = lists[i]
            if (ptrs[i]): PQ.append((ptrs[i].val, i))                        
        
        PQ.sort(reverse=True)
        ret = cur = None
        # Using priority queue, pop every new insert
        # After inserting a pop, move to next of that list
        # PQ sorted in descending order
        
        while PQ:
            val, ind = PQ.pop()
            ptrs[ind] = ptrs[ind].next
            
            if (ret == None):
                ret = ListNode(val)
                cur = ret
            else:
                cur.next = ListNode(val)
                cur = cur.next
            
            if (ptrs[ind] is not None):
                self.insertQueue(ptrs[ind].val, ind, PQ)
            
        return ret
    
    def insertQueue(self, elem, index, PQ):
        
        if (len(PQ) == 0 or elem < PQ[-1][0]):
            PQ.append((elem, index))
            return 
        
        for i in xrange(len(PQ)):
            if (PQ[i][0] < elem): break
        
        PQ.insert(i, (elem, index))
        
        
