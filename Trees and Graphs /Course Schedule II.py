from collections import defaultdict

# DAG - topological sorting
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list( range(numCourses) )

        adj_lit = defaultdict(list)
        for c0, c1 in prerequisites:
            adj_lit[c0].append(c1)

        def traverse(c0):
            '''check a vertix's prerequisite'''
            visited[c0] = True
            for cs in adj_lit[c0]:
                if not visited[cs]:
                    traverse(cs) # DFS
            stack.append(c0)

        visited = [False] * numCourses
        stack = []
        adj_keys = list(adj_lit.keys()) # to handle defaultdict's size changed during iteration in line-12
        for c0 in adj_keys:
            if not visited[c0]:
                traverse(c0)
        
        return stack
# Failed at task like:
#   n = 2
#   prerequisites = [[0,1],[1,0]]
            
###
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        for c0, c1 in prerequisites:
            adj_list[c0].append(c1)
        
        output = []
        for c0 in range(numCourses):
            if adj_list[c0] == []:
                output.append(c0)
            else:
                # do DFS
                pass
###

###
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        for c0, c1 in prerequisites:
            adj_list[c0].append(c1)

        def DFS(c0, master):
            visited[c0] = True
            for c1 in adj_list[c0]:
                # detect loop (cycle)
                if adj_list[c1] == master:
                    acycle[0] = False

                if not visited[c1]:
                    DFS(c1, master)
            
            output.append(c0)
                    
        visited = [False] * numCourses
        output = []
        acycle = [True]
        for c0 in range(numCourses):
            if acycle[0] == False:
                return []
            
            if not visited[c0]:
                # independent course
                if adj_list[c0] == []:
                    visited[c0] = True
                    output.append(c0)

                else:
                    DFS(c0, c0)
        return output
###

###### still failed at n=2, pre=[[0,1],[1,0]] ######  
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        for c0, c1 in prerequisites:
            adj_list[c0].append(c1)

        def DFS(c0, master):
            visited[c0] = True
            for c1 in adj_list[c0]:
                # detect loop (cycle)
                if adj_list[c1] == master:
                    acycle[0] = False

                if not visited[c1]:
                    DFS(c1, master)
            
            output.append(c0)
                    
        visited = [False] * numCourses
        output = []
        acycle = [True]
        for c0 in range(numCourses):
            if acycle[0] == False:
                return []
            
            if not visited[c0]:
                # independent course
                if adj_list[c0] == []:
                    visited[c0] = True
                    output.append(c0)

                else:
                    DFS(c0, c0)
        return output    
###### still failed at n=2, pre=[[0,1],[1,0]] ######  
        

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for next_c, pre_c in prerequisites:
            graph[pre_c].append(next_c)
            in_degree[next_c] += 1
            
        BFS_q = deque()
        for cs in range(numCourses):
            if in_degree[cs] == 0:
                BFS_q.append(cs)
        
        ans = []
        while BFS_q:
            curr = BFS_q.popleft()
            ans.append(curr)
            for next_c in graph[curr]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    BFS_q.append(next_c)
        
        return ans if len(ans)==numCourses else []
        
        
