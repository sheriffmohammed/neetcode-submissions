class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                P = parent[p]
            
            return p

        def union(n1,n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
            return True
        for i,j in edges:
            if not union(i,j):
                return False
        for i in parent:
            if i != parent[0]:
                return False
        return True
