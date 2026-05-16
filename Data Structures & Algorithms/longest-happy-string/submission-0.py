class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s , maxHeap = "" , []
        for v,c in ((-a,'a'),(-b,'b'),(-c,'c')):
            if v:
                heapq.heappush(maxHeap,(v,c))
        
        while maxHeap:
            count , c = heapq.heappop(maxHeap)
            print(s,c)
            if len(s) > 1 and s[-1] == s[-2] == c:
                if not maxHeap:
                    break
                count2 , c2 = heapq.heappop(maxHeap)
                s += c2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap,(count2,c2))
            else:
                s += c
                count += 1
            if count:
                heapq.heappush(maxHeap,(count,c))
        return s       