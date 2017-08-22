# Friend circles Python 

# My solution ran super slow compared to everyone else (beats 14.47% :()
# I did not use a DFS, instead I went through the two columns, when
# a new friend joined the circle I added him to my queue and would explore him later. 

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        size = len(M)
        circles = 0
        starting_list = []
        
        for i in range(size):
            for j in range(size):
                # Friend not by himself
                if (M[i][j] == 1 and (i != j)):
                    M[i][j] = -1
                    starting_list.append(i)
                    starting_list.append(j)
                    self.modify(M, starting_list)
                    circles += 1
                    
        for i in range(size):
            for j in range(size):
                if (M[i][j] == 1):
                    circles += 1
        
        return circles
    
    def modify(self, M, starting_list):
        
        while (len(starting_list) > 0):    
            cur = starting_list.pop(0)
            for iterate in range(0, len(M)):
                if (M[iterate][cur] == 1):
                    M[iterate][cur] = -1
                    M[cur][iterate] = -1
                    if (iterate != cur):
                        starting_list.append(iterate)   
