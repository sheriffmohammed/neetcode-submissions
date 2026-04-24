class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        count = n
        def find(node):
            return parent[node]
                 
        def union(n1,n2):
            n1 , n2 = find(n1) , find(n2)
            if find(n1) == find(n2):
                return False
            if rank[n1] > rank[n2]:
                parent[n2] = n1
            elif rank[n1] < rank[n2]:
                parent[n1] = n2
            else:
                parent[n2] = n1
                rank[n1] += 1
            return True

        for i , j in edges:
            if union(i,j):
                count -= 1
        return count        