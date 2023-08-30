class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for src, dest in edges:
            self.adjList[src].append(dest)
    
def is_reachable(graph, v1, v2):
    '''
    BFS to visit vertices.
    If it doesn't meet the designated vertix, it's not connected.
    '''
    queue = []
    visit = [False] * len(graph.adjList)

    queue.append(v1)
    
    while queue:
        if not visit[queue[0]]:
            current = queue.pop(0)
            visit[current] = True

            for node in graph.adjList[current]:
                if not visit[node]:
                    queue.append(node)
                if node == v2:
                    return True
    return False


import unittest
from collections import deque
# VISUAL OF TEST GRAPH

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O  I -- J -- K
#              |
#              L

# P -- Q
# |  /
# R

class GraphA(Graph):
    def __init__(self, edges):
        self.adjListA = dict()
        
        for start, end in edges:
            if start not in self.adjListA.keys():
                self.adjListA[start] = [end]
            else:
                self.adjListA[start].append(end)
    
    def __repr__(self):
        _str = ''
        for k, v in self.adjListA.items():
            _str += f'{k}: {v}\n'
        return _str

if __name__ == '__main__':
    edges1 = [
        (1,0), (1,4), (1,2), (2,7), (4,3), (4,6), (0,3), (3,5), (5,6), (6,7),
        (8,9), (9,10), (10,8),
    ]
    n1 = 8+3
    graph1 = Graph(edges1, n1)
    print(len(graph1.adjList))

    print(is_reachable(graph1, 0, 7))
    print(is_reachable(graph1, 8, 9))
    print(is_reachable(graph1, 0, 10))

    print('Test GraphA')
    edges2 = [('A','B'), ('A','C'), ('A','B')]
