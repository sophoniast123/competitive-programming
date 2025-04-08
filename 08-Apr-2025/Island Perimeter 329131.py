# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,-1), (0,1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        def inbound(r,c):
            return 0<=r<m and 0<=c<n
        visited = set()
        par = 0
        def dfs (row,col,visited):
            nonlocal par
            visited.add((row,col))
            for r_c, c_c in directions:
                n_r = row + r_c
                n_c = col + c_c

                if inbound(n_r, n_c) and grid[n_r][n_c]:
                    if (n_r,n_c) not in visited:
                        dfs(n_r, n_c, visited)
                else:
                    par += 1
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c,visited)
                    return par
        return 0