# My thought is to do DP from outer part all the way to the center

# (0,0), (0,1)
# (1,0), (1,1)

# First round
# (0,0) to (0,len(heights[0])-1)
# (0,0) to (len(heights)-1,0)
# (0,len(heights[0])-1) to (len(heights)-1,len(heights[0])-1)
# (len(heights)-1,0) to (len(heights)-1,len(heights[0])-1)

# Second round
# (0+1,0+1) to (0+1,len(heights[0])-1-1)
# (0+1,0+1) to (len(heights)-1-1,0+1)
# (0+1,len(heights[0])-1-1) to (len(heights)-1-1,len(heights[0])-1-1)
# (len(heights)-1-1,0+1) to (len(heights)-1-1,len(heights[0])-1-1)

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # to record our route for DP
        DP = [
            [
                {'P': False, 'A': False} for _ in range(len(heights[0]))
            ] for _ in range(len(heights))
        ]
        output = []

        def check_a_cell(r0, c0):
            stack = deque((r0, c0))
            # BFS
            while stack:
                # current cell
                r, c = stack.popleft()
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    # at the boundary
                    if r+dr in [-1, len(heights)] or c+dc in [-1, len(heights[0])]:
                    
                        if r+dr == -1:
                            DP[r0][c0]['P'] == True
                        elif r+dr == len(heights):
                            DP[r0][c0]['A'] == True
                        
                        if c+dc == -1:
                            DP[r0][c0]['P'] == True
                        elif c+dc == len(heights[0]):
                            DP[r0][c0]['A'] == True

                        if DP[r0][c0]['A'] and DP[r0][c0]['P']:
                            output.append([r0, c0])
                            return
                        
                    else:
                        # meet the flowing condition
                        if heights[r+dr][c+dc] <= heights[r][c]:
                            if DP[r+dr][c+dc]['P']:
                                DP[r0][c0]['P'] = True
                            if DP[r+dr][c+dc]['A']:
                                DP[r0][c0]['A'] = True
                            if DP[r0][c0]['A'] and DP[r0][c0]['P']:
                                output.append([r0, c0])
                                return
                            stack.append((r+dr, c+dc))

        ceil = 0
        floor = len(heights)-1
        left = 0
        right = len(heights[0])-1
        while True:
            # ceil
            for c in range(left, right+1):
                pass


# My thought is to do DP from outer part all the way to the center

# (0,0), (0,1)
# (1,0), (1,1)

# First round
# (0,0) to (0,len(heights[0])-1)
# (0,0) to (len(heights)-1,0)
# (0,len(heights[0])-1) to (len(heights)-1,len(heights[0])-1)
# (len(heights)-1,0) to (len(heights)-1,len(heights[0])-1)

# Second round
# (0+1,0+1) to (0+1,len(heights[0])-1-1)
# (0+1,0+1) to (len(heights)-1-1,0+1)
# (0+1,len(heights[0])-1-1) to (len(heights)-1-1,len(heights[0])-1-1)
# (len(heights)-1-1,0+1) to (len(heights)-1-1,len(heights[0])-1-1)

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # to record our route for DP
        DP = [
            [
                {'P': False, 'A': False, 'traveled': False} for _ in range(len(heights[0]))
            ] for _ in range(len(heights))
        ]
        output = []

        def check_a_cell(r0, c0):
            stack = deque((r0, c0))
            # BFS
            while stack:
                # current cell
                r, c = stack.popleft()
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    # at the boundary
                    if r+dr in [-1, len(heights)] or c+dc in [-1, len(heights[0])]:
                    
                        if r+dr == -1:
                            DP[r0][c0]['P'] == True
                        elif r+dr == len(heights):
                            DP[r0][c0]['A'] == True
                        
                        if c+dc == -1:
                            DP[r0][c0]['P'] == True
                        elif c+dc == len(heights[0]):
                            DP[r0][c0]['A'] == True

                        if DP[r0][c0]['A'] and DP[r0][c0]['P']:
                            output.append([r0, c0])
                        
                    else:
                        # meet the flowing condition
                        if heights[r+dr][c+dc] <= heights[r][c]:
                            if DP[r+dr][c+dc]['P']:
                                DP[r0][c0]['P'] = True
                            if DP[r+dr][c+dc]['A']:
                                DP[r0][c0]['A'] = True
                            if DP[r0][c0]['A'] and DP[r0][c0]['P']:
                                output.append([r0, c0])
                                return
                            stack.append((r+dr, c+dc))

        ceil = 0
        floor = len(heights)-1
        left = 0
        right = len(heights[0])-1
        while True:
            # ceil
            for c in range(left, right+1):
                pass


# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         traveled_dict = dict()
#         route_dict = dict()
#         stack_dict = dict()
#         for r in range(len(heights)):
#             for c in range(len(heights[0])):
#                 traveled_dict[f'{r}{c}'] = {'traveled': False}
#                 route_dict[f'{r}{c}'] = {'A': False, 'P': False}
#                 stack_dict[f'{r}{c}'] = True
        
#         r = 0
#         # BFS for cell
#         while stack_dict:
#             # go right
#             c = 0
#             while True:
#                 for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#                     traveled_dict[]
#                     # at the boundary
#                     if r+dr == -1 or c+dc == -1:
#                         route_dict[f'{r}{c}']['P'] = True
#                     if r+dr == len(heights) or c+dc == len(heights[0]):
#                         route_dict[f'{r}{c}']['C'] = True
            

######################################################################################################3
# DFS
# Check route from the border and DFS into the center. Seperate check for Atlantic and Pacific.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        atlantic = set()
        pacific = set()
        
        def traverse(r, c, check_set):
            if (r, c) in check_set:
                return
            check_set.add((r, c)) 
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = r+dr
                new_c = c+dc
                # check if new_r and new_c are valid
                if 0<=new_r<len(heights) and 0<=new_c<len(heights[0]):
                    # if it's sourcible
                    if heights[new_r][new_c]>=heights[r][c]:
                        traverse(new_r, new_c, check_set)
        
        # border traverse
        for r in range(len(heights)):
            traverse(r, 0, pacific) # left
            traverse(r, len(heights[0])-1, atlantic) # right
        for c in range(len(heights[0])):
            traverse(0, c, pacific) # top
            traverse(len(heights)-1, c, atlantic) # bottom
        
        return list(pacific & atlantic)
            
        
