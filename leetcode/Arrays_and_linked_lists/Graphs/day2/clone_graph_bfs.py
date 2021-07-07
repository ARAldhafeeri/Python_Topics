"""
Runtime: 32 ms, faster than 93.79% of Python3 online submissions for Clone Graph.
Memory Usage: 14.5 MB, less than 81.22% of Python3 online submissions for Clone Graph.

Accepted
494.9K
Submissions
1.2M

Q:
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

nput: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

constrains:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visted_nodes = set()
        queue = [node] # first in first out FIFO
        # preform bfs to get all unique visted nodes.
        while queue:
            tmp = queue.pop()
            visted_nodes.add(tmp.val)
            for edge in tmp.neighbors: # check all nodes edges
                if edge.val not in visted_nodes:
                    queue.append(edge)
        clone = collections.defaultdict(list) # so we don't get key error
        clone = {i: Node(i) for i in visted_nodes} # copy all nodes
        visted_nodes = set()
        queue = [node]
        while queue: # breform bfs again but this time in give cloned nodes its neighbors.
            tmp = queue.pop()
            visted_nodes.add(tmp.val)
            # take every node and give it its neighbors
            clone[tmp.val].neighbors = [clone[edge.val] for edge in tmp.neighbors]
            for edge in tmp.neighbors:
                if edge.val not in visted_nodes:
                    queue.append(edge)
        return clone[node.val]