# Leetcode: https://leetcode.com/problems/the-maze/description/
# I wanted to upload maze2 but I TLE'd on it, you need to use dijkstra and it's not an algorithm I recall.
# DFS for speed, just roll in 4 directions and insert into DFS the new positions.
# Beats 70%

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # Save the co-ordinates (if we repeat, we don't roll)
        loc_x, loc_y = start[0], start[1]
        dest_x, dest_y = destination[0], destination[1]
        
        seen = {}
        queue = [(loc_x, loc_y)]
        
        while (queue):
            x,y = queue.pop()
            seen[(x, y)] = 1

            if (x == dest_x and y == dest_y): return True     
            nxt = [0] * 4

            # Roll right
            for i in xrange(y, len(maze[0])):
                if (maze[x][i] == 1): 
                    i -= 1
                    break

            nxt[0] = ((x, i))
            
            # Roll left
            for i in xrange(y, -1, -1):
                if (maze[x][i] == 1): 
                    i += 1
                    break
        
            nxt[1] = ((x, i))
            
            # Rolling down
            for i in xrange(x, len(maze)):
                if (maze[i][y] == 1): 
                    i -= 1
                    break

            nxt[2] = ((i, y))

            # Rolling up
            for i in xrange(x, -1, -1):
                if (maze[i][y] == 1): 
                    i += 1
                    break
                
            nxt[3] = ((i, y))
            
            for i in xrange(len(nxt)):
                if (nxt[i] not in seen):
                    queue.append(nxt[i])
            
        return False
