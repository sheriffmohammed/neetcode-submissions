class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {}
        indegree = {}
        q = deque([])

        for i,j in edges:
            if i not in adjList:
                adjList[i] = []
            if j not in adjList:
                adjList[j] = []
            adjList[i].append(j)
            adjList[j].append(i)

            if i not in indegree:
                indegree[i] = 0
            if j not in indegree:
                indegree[j] = 0
            indegree[i] +=1
            indegree[j] +=1
                
        for k,v in indegree.items():
            if v == 1:
                q.append(k)
        while q:
            node = q.popleft()
            indegree[node] -=1
            for n in adjList[node]:
                indegree[n] -= 1
                if indegree[n] == 1:
                    q.append(n)

        for i,j in reversed(edges):
            if indegree[i] >= 1 and indegree[j] >= 1:
                return [i,j]
        return []                 