class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 0:
            return True
        
        adjList = {i:[] for i in range(n)}
        visited = set()        
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        def dfs(node,prev):
            if node in visited:
                return False
            
            visited.add(node)     
            
            if not adjList[node]:
                return True
            
            for i in adjList[node]:
                if i == prev:
                    continue
                if not dfs(i,node):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)           

            
        
