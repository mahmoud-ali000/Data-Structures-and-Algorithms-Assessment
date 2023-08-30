from typing import List
from collections import deque


# Brute Force TLE
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                
                if mat[r][c] != 1:
                    continue

                #BFS
                queue.append((r, c, 0))
                while queue:
                    new_r, new_c, dis = queue.popleft()
                    for mv_r, mv_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        if 0 <= new_r+mv_r < len(mat) and 0 <= new_c+mv_c < len(mat[0]):
                            if mat[new_r+mv_r][new_c+mv_c] == 0:
                                mat[r][c] = dis+1
                                queue = deque()
                                break
                            else:
                                queue.append((new_r+mv_r, new_c+mv_c, dis+1))
    
        return mat


# optimized BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # track all 0 first
        nodes = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    nodes.append((r, c, 0))

        # [
        #     [0,0,0],
        #     [0,1,0],
        #     [1,1,1],
        #     [1,1,1]
        # ]

        visited = [
            [False] * len(mat[0]) for _ in range(len(mat))
        ]
        # BFS
        while nodes:
            r, c, dis = nodes.popleft() # with original mat value

            if visited[r][c]: continue
            visited[r][c] = True

            # update value
            mat[r][c] = dis

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                # node exists
                if 0<=r+dr<len(mat) and 0<=c+dc<len(mat[0]):
                    nodes.append((r+dr, c+dc, dis+1))
        
        return mat
print(Solution().updateMatrix(
    [
        [0,0,0],
        [0,1,0],
        [1,1,1],
        [1,1,1]
    ]
))
