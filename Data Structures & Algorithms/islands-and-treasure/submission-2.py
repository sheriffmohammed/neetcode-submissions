class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        level = 1
        while q:
            for i in range(len(q)):
                R , C = q.popleft()
                for i in directions:
                    r , c = R+i[0],C+i[1]
                    if (r in range(rows)and
                        c in range(cols)and
                        (r,c) not in visited and
                        grid[r][c] > 0):
                        q.append((r,c))
                        visited.add((r,c))
                        grid[r][c] = level
            level += 1
