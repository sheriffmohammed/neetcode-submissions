class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows , cols = len(grid) , len(grid[0])
        res = [0]

        def dfs(r,c):
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] == 0
                ):
                return 1
            if  (r,c) in visited:
                return 0    

            visited.add((r,c))

            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)