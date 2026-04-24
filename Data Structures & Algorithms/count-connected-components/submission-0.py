class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        q = []
        visited = set()
        adjList = {i:[] for i in range(n)}
        self.res = 0
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        def bfs(n):
            q.append(n)
            self.res += 1
            while q:
                node = q.pop(0)
                visited.add(node)
                for i in adjList[node]:
                    if i not in visited:
                        q.append(i)

        for i in adjList.keys():
            if i not in visited:
                bfs(i)
        return self.res                        
