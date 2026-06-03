class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r,c):
            if(
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                (r,c) in visited or
                grid[r][c] == 0
            ):
                return 0
            
            visited.add((r,c))
             
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] != 0:
                    res = max(dfs(i,j),res)
        return res