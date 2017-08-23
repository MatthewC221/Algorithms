# Leetcode graph division, was okay but I spent a decent amount of time remembering how to create
# Py classes. I thought it would be really slow but I beat 55.5 % which is decent.
# To do this question efficiently I think you need to use a graph.

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = Graph()
        seen = {}                           # Keep track of possible nodes for early exits
        for i in range(len(equations)):
            seen[equations[i][0]] = 1
            seen[equations[i][1]] = 1
            graph.addEdge(Edge(equations[i][0], equations[i][1], values[i]))
            graph.addEdge(Edge(equations[i][1], equations[i][0], float(1) / values[i]))
        
        # Perform DFS
        explored = {}
        queue = []
        return_list = []
         
        # DFS for each query
        for i in range(len(queries)):
            if (queries[i][0] not in seen or queries[i][1] not in seen):
                return_list.append(-1.0)
            elif (queries[i][0] == queries[i][1]):
                return_list.append(1.0)
            else:
                queue.append((queries[i][0], 1.0))
                dest = queries[i][1]
                explored.clear()
                flag = False
                while (len(queue) > 0):
                    tmp = queue.pop()
                    name = tmp[0]           # Name of current node
                    val = tmp[1]            # Weight value currently
                    explored[name] = 1
                    if (name == dest):
                        return_list.append(val)
                        del queue[:]
                        flag = True
                    else:
                        adjacent = graph.getAllEdges(name)
                        # Multiply the new weight
                        for i in range(len(adjacent)):
                            if (adjacent[i][0] not in explored):
                                queue.append((adjacent[i][0], val * adjacent[i][1]))
                # No path available
                if (flag == False):             
                    return_list.append(-1.0)
        
        # For some reason, (leetcode?), I had to reset the edges even though
        # I initialised graph = Graph()
        graph.deleteEdges()
        return return_list
        
            
class Graph(object):
    edges = []
    def addEdge(self, edge):
        self.edges.append(edge)
    def printEdges(self):
        for i in range(len(self.edges)):
            print self.edges[i].source,
            print self.edges[i].dest,
            print self.edges[i].weight
    def getAllEdges(self, source):
        adjacent = []
        for i in range(len(self.edges)):
            if (self.edges[i].source == source):
                adjacent.append((self.edges[i].dest, self.edges[i].weight))
     
        return adjacent
    def deleteEdges(self):
        del self.edges[:]
    
class Edge(object):
    def __init__(self, _from, _to, weight):
        self.source = _from
        self.dest = _to
        self.weight = weight
