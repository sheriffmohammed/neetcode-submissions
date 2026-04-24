class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        q = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])

        def bfs():
            dist = 1
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    for dr , dc in directions:
                        r = row + dr
                        c = col + dc
                        if (r in range(rows) and c in range(cols) and 
                           (r,c) not in visited and grid[r][c] > 200):
                            q.append([r,c])
                            grid[r][c] = dist
                            visited.add((r,c))
                dist += 1
        bfs()                       

