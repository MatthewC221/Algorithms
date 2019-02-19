# Leetcode: https://leetcode.com/problems/satisfiability-of-equality-equations/
# LC Medium: Optimised approach beats 91%
"""
Naive approach
1. Equality step: Create separate graphs for equality (each node in one graph has the same value)
2. Satisfiability step: Check that we can't get from A->B

Naive because we might be traversing the same graph multiple times. O(n^2) at worst

Optimised:
1. Equality step: Create separate graphs for equality (each node in one graph has the same value)
2. Preprocess step: Assign values for each graph s.t. all values in graph 1 have value = 1, all values in graph 2 have value = 2
3. Satisfiability step: Look up simple dictionary that a != b.

O(n) as each element is iterated over only once
"""

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
     
        neighbours = {}
        assigned_values = {}
        starting_points = []
        # 1. Graph creation step, create graphs in Python dictionary 
        for equation in equations:
            var1, var2 = equation[0], equation[3]
            if equation[1] == "=":
                if var1 == var2: continue
                # Setting up neighbours
                if var1 not in neighbours: 
                    neighbours[var1] = [var2]
                else: 
                    if var2 not in neighbours[var1]:
                        neighbours[var1].append(var2)
                        
                if var2 not in neighbours: 
                    neighbours[var2] = [var1]
                else: 
                    if var1 not in neighbours[var2]:
                        neighbours[var2].append(var1)
                
                # Flagging nodes that have assignments
                if var1 not in assigned_values: 
                    assigned_values[var1] = 0
                    starting_points.append(var1)
                if var2 not in assigned_values: assigned_values[var2] = 0
                
        uniq_value = 1
        visited = {}
        # 2. Preprocess step: Colour each graph using a diff value
        # E.g. All nodes of graph 1 have value 1, all values of graph 2 have value 2
        for node in starting_points:
            if assigned_values[node] != 0: continue
            visited[node] = True
            stk = [node]
            while stk:
                cur = stk.pop()
                assigned_values[cur] = uniq_value
                for nxt_node in neighbours[cur]:
                    if nxt_node not in visited:
                        stk.append(nxt_node)
                        visited[nxt_node] = True
            
            uniq_value += 1
        
        # 3. Satisfiability step: Simple dictionary lookups (some special cases)
        for equation in equations:
            var1, var2 = equation[0], equation[3]
            if equation[1] == "!":
                if var1 == var2: return False
                if var1 not in assigned_values or var2 not in assigned_values: continue
                if assigned_values[var1] == assigned_values[var2]: return False
        
        return True
            
                
