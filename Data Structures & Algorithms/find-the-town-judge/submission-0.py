class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashmap = {x:[] for x in range(1,n+1)}
        hashset = set()
        for i , j in trust:
            hashmap[j].append(i)
            hashset.add(i)

        for i , j in hashmap.items():
            if len(j) == n - 1 and i not in hashset:
                return i
        return -1            
