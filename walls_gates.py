# Leetcode: https://leetcode.com/problems/walls-and-gates/description/
# Both of these time out on test 61/62. I even have a memoization one running but I think the append to list is too expensive.
# Not entirely sure how I would make it faster.

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        # BFS to a gate, with DP style memoization
        if not rooms: return
        
        m = len(rooms)
        n = len(rooms[0])
        count = 0
        
        for i in xrange(m):
            for j in xrange(n):
                if (rooms[i][j] == 2147483647):         # Only BFS for rooms that have no current path to goal 
                    self.BFS(rooms, i, j)
    
    """"""
    def BFS(self, rooms, loc_x, loc_y):
        
        queue = [(loc_x, loc_y, 0)]
        m = len(rooms)
        n = len(rooms[0])
        fast = 2147483647
        H = {}
        
        while queue:
            new = []
            for i in xrange(len(queue)):
                x, y, dist = queue[i]
                if (rooms[x][y] == 0):
                    fast = min(fast, dist)
                    new = []
                    break
                elif (rooms[x][y] > 0 and rooms[x][y] < 2147483647):
                    fast = min(fast, dist + rooms[x][y])
                else:
                    nxt = [0] * 4
                    nxt[0] = (x + 1, y)
                    nxt[1] = (x - 1, y)
                    nxt[2] = (x, y + 1)
                    nxt[3] = (x, y - 1)
                    for j in xrange(len(nxt)):
                        if (self.isValid(nxt[j][0], nxt[j][1], m, n)):
                            if (rooms[nxt[j][0]][nxt[j][1]] != -1 and ((nxt[j][0], nxt[j][1]) not in H)):
                                new.append((nxt[j][0], nxt[j][1], dist+1))
                                H[(nxt[j][0], nxt[j][1])] = 1
            queue = new
        
        rooms[loc_x][loc_y] = fast
        
    
    """
    def BFS(self, rooms, i, j):
        
        cur_path = [(i, j)]
        queue = [[cur_path, 0]]     # Starting distance = 0, keep track of all visited nodes so we can backtrack and memoize
        H = {}
        
     #   print (i, j)
        
        m = len(rooms)
        n = len(rooms[0])
        mx = sys.maxint
        saved = []
        
        # BFS to find shortest path
        while queue:
            new = []
            for i in xrange(len(queue)):
                x, y = queue[i][0][-1]
                dist = queue[i][1]
 
                if (rooms[x][y] == 0):
                    if (dist < mx):
                        saved = queue[i][0]
                        mx = dist
                    new = []
                    break

                if (rooms[x][y] > 0 and rooms[x][y] != 2147483647): 
                    if (dist + rooms[x][y] < mx): 
                        saved = queue[i][0]
                        mx = dist + rooms[x][y]
               #     print mx
                else:               
                    nxt = [0] * 4
                    nxt[0] = (x + 1, y)
                    nxt[1] = (x - 1, y)
                    nxt[2] = (x, y + 1)
                    nxt[3] = (x, y - 1)

                    for j in xrange(len(nxt)):
                        if (self.isValid(nxt[j][0], nxt[j][1], m, n)):
                            if (rooms[nxt[j][0]][nxt[j][1]] != -1 and ((nxt[j][0], nxt[j][1]) not in H)):
                                path = queue[i][0][:]
                                path.append((nxt[j][0], nxt[j][1]))
                                new.append((path, dist+1))
                                H[(nxt[j][0], nxt[j][1])] = 1
            queue = new
        
        for k in xrange(len(saved)):
            loc_x, loc_y = saved[k]
            rooms[loc_x][loc_y] = mx - k
    """
    
    def isValid(self, i, j, m, n):
        
        return i >= 0 and i < m and j >= 0 and j < n
            
