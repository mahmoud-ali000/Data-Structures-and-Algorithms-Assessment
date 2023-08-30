# find the unconnected graphs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        length = len(grid[0])

        discovered_grid = []
        for r in range(height):
            discovered_grid.append([])
            for c in range(length):
                discovered_grid[r].append(False)
        
        islands = 0

        r = 0
        while r < height:
            
            c = 0
            while c < length:
                if discovered_grid[r][c] is False and grid[r][c] == "1":
                    islands += 1
                    # start BFS
                    islands_q = [(r, c)]
                    while islands_q:
                        cr, cc = islands_q.pop(0)
                        discovered_grid[cr][cc] = True

                        # top
                        if cr-1 >=0:
                            if discovered_grid[cr-1][cc] is False and grid[cr-1][cc] != "0":
                                islands_q.append((cr-1, cc))
                        # right
                        if cc+1 <=length-1:
                            if discovered_grid[cr][cc+1] is False and grid[cr][cc+1] != "0":
                                islands_q.append((cr, cc+1))
                        # bottom
                        if cr+1 <=height-1:
                            if discovered_grid[cr+1][cc] is False and grid[cr+1][cc] != "0":
                                islands_q.append((cr+1, cc))
                        # left
                        if cc-1 >=0:
                            if discovered_grid[cr][cc-1] is False and grid[cr][cc-1] != "0":
                                islands_q.append((cr, cc-1))
                else:
                    discovered_grid[r][c] = True
                c += 1
            r += 1
        return islands
# Time Limit Exceeded

#######################################################################################################################################
                
# find the unconnected graphs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        length = len(grid[0])
        
        islands = 0

        r = 0
        while r < height:
            
            c = 0
            while c < length:
                if grid[r][c] == "1":
                    islands += 1
                    # start BFS
                    islands_q = [(r, c)]
                    while islands_q:
                        cr, cc = islands_q.pop(0)
                        grid[cr][cc] = "checked"

                        # top
                        if cr-1 >=0:
                            if grid[cr-1][cc] == "1":
                                islands_q.append((cr-1, cc))
                        # right
                        if cc+1 <=length-1:
                            if grid[cr][cc+1] == "1":
                                islands_q.append((cr, cc+1))
                        # bottom
                        if cr+1 <=height-1:
                            if grid[cr+1][cc] == "1":
                                islands_q.append((cr+1, cc))
                        # left
                        if cc-1 >=0:
                            if grid[cr][cc-1] == "1":
                                islands_q.append((cr, cc-1))
                else:
                    grid[r][c] = "checked"
                c += 1
            r += 1
        return islands
# Time Limit Exceeded

#######################################################################################################################################

# Python Simple DFS Solution
# https://leetcode.com/problems/number-of-islands/solutions/56340/python-simple-dfs-solution/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_n = 0
        for r in range( len(grid) ):
            for c in range( len(grid[0]) ):
                if grid[r][c] == "1":
                    islands_n += 1
                    self.dfs(grid, r, c)
                else:
                    grid[r][c] = "checked"
        return islands_n
    
    def dfs(self, grid, r, c):
        if r<0 or c<0 or r>len(grid)-1 or c>len(grid[0])-1 or grid[r][c] in ["checked", "0"]:
            return
        
        grid[r][c] = "checked"

        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)
