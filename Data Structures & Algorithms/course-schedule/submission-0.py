class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visited = set()
        indegree = [0 for i in range(numCourses)]
        q = deque([])

        for i in range(numCourses):
            adjList[i] = []
        for i,j in prerequisites:
            adjList[j].append(i)
            indegree[i] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node =  q.popleft()
            visited.add(node)
            for i in adjList[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)


        return len(visited) == numCourses