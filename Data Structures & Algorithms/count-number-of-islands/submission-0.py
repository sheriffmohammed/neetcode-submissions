class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        row,col = len(grid) , len(grid[0])
        
        def dfs(r,c):
            if( r < 0 or
                c < 0 or
                r >= row or
                c >= col or
                (r,c) in visited or
                grid[r][c] == '0'):
                return 

            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] != '0':
                    res += 1
                    dfs(i,j)
        return res                
                