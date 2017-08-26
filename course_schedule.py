# Leetcode: https://leetcode.com/problems/course-schedule/description/
# I exceeded time limit on this, however I'm quite sure it's correct as I passed the first 32/37 tests (TLE on 33/37)
# This requires a topological sorting graph (never used one).
# My technique was DFS but check if I explored all the prereqs before exploring a course (lots of overhead)

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Make a graph, then do a DFS / BFS to see if course 0 can reach course 1 
        g = Graph(prerequisites)
        
        # There requires something that has no prerequisites
        
        prereq = {}         # Dict of all prereqs
        to_do = {}          # Dict of all courses need to complete
        for i in range(len(prerequisites)):
            prereq[prerequisites[i][1]] = 1
            to_do[prerequisites[i][0]] = 1
        
        diff = set(prereq.keys()) - set(to_do.keys())
        start = list(diff)
        explored = {}
        
        while (len(start) > 0):
            tmp = start.pop()
            req, dest = g.getAll(tmp)
            
            flag = True
            for pq in req:
                if (pq not in explored):
                    flag = False
            
            if (flag == True):  
                explored[tmp] = 1
                to_do.pop(tmp, None)
                for node in dest:
                    if (node not in explored):
                        start.append(node)
        
        return len(to_do) == 0
        
            
class Graph(object):
    edges = [[]]
    def __init__(self, lst):
        self.edges = lst
    
    def getAllCourses(self, source):
        ret = []
        for i in range(len(self.edges)):
            if (self.edges[i][1] == source):
                ret.append(self.edges[i][0])
    
        return ret
    
    def getAll(self, source):
        req = []
        dest = []
        for i in range(len(self.edges)):
            if (self.edges[i][1] == source):
                dest.append(self.edges[i][0])
            elif (self.edges[i][0] == source):
                req.append(self.edges[i][1])
    
        return (req, dest)
    
    def getAllPre(self, source):    # Get all prereqs for a course
        
        ret = []
        for i in range(len(self.edges)):
            if (self.edges[i][0] == source):
                ret.append(self.edges[i][1])
        
        return ret
