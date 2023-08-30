from collections import deque


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        graph = Node(node.val)
        visited = set()

        ori_queue = deque([node])
        copy_queue = deque([graph])

        while ori_queue:
            ori_curr = ori_queue.popleft()
            copy_curr = copy_queue.popleft()
            if ori_curr.val in visited:
                continue
            visited.add(ori_curr.val)
            print(graph.val, graph.neighbors)
            for nb in ori_curr.neighbors:
                copy_node = Node(nb.val)
                copy_curr.neighbors.append(copy_node)

                copy_queue.append(copy_node)
                ori_queue.append(nb)
        print(graph.neighbors[0].val, graph.neighbors[0].neighbors[0].val)
        return graph
# input [[2],[1]]
# You must return a copy of all the nodes in the original graph

# debug with
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        graph = Node(node.val)
        visited = set()

        ori_queue = deque([node])
        copy_queue = deque([graph])

        while ori_queue:
            ori_curr = ori_queue.popleft()
            copy_curr = copy_queue.popleft()
            if ori_curr.val in visited:
                continue
            visited.add(ori_curr.val)

            for nb in ori_curr.neighbors:
                copy_node = Node(nb.val)
                copy_curr.neighbors.append(copy_node)

                copy_queue.append(copy_node)
                ori_queue.append(nb)
        print(graph.val, graph.neighbors)
        print(graph.neighbors[0].val, graph.neighbors[0].neighbors)
        print(graph.neighbors[0].neighbors[0] == graph)
        return graph
# found the problem, 
"""
1 [<__main__.Node object at 0x7f4c8e493910>]
2 [<__main__.Node object at 0x7f4c8e493ee0>]
False
"""
# graph.neighbors[0].neighbors[0] == graph: False
# it's the problem


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        visited = set()
        graph = Node(node.val)
        queue = deque([node])
        node_map = {graph.val: graph}

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            for nb in current.neighbors:
                if nb.val not in node_map:
                    node_map[nb.val] = Node(nb.val)
                node_map[current.val].neighbors.append( node_map[nb.val] )
                queue.append( nb )
   
        return graph
            
            
