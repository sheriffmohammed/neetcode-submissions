class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 0:
            return True
        
        adjList = {i:[] for i in range(n)}
        q = deque([0])
        visited = set()        
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        prev = -1
        
        while q:
            for i in range(len(q)):
                node = q.pop()
                if node in visited:
                    print(visited,node)
                    return False
                visited.add(node)
                for j in adjList[node]:
                    if j == prev:
                        continue
                    q.append(j)
            prev = node
        
        return len(visited) == n        
