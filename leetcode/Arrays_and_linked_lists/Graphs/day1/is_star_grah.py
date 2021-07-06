


"""
Runtime: 840 ms, faster than 40.18% of Python3 online submissions for Find Center of Star Graph.
Memory Usage: 50.3 MB, less than 61.03% of Python3 online submissions for Find Center of Star Graph.
sol 1:
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        nodes = {i: 0 for i in range(1, n+1)}
        isStar = len(edges)
        for i,j in edges: # count links for each node
            nodes[i], nodes[j] = nodes[i] +1, nodes[j] + 1
        for k,v in nodes.items():
            if v == isStar:
                return k
        
            
"""
sol 1 refactored :
"""
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        links = [0] * (len(edges) + 1)  # count links, also each index is the vertex
        isStar = len(edges)
        for i,j in edges: # count links for each node
            links[i - 1], links[j - 1] = links[i-1] +1, links[j-1] + 1
        return links.index( max(links) ) + 1
"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

"""