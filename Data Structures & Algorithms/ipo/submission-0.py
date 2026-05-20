class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap , minHeap = [] , []
        res = 0
        init = w 

        for i,(c,p) in enumerate(zip(capital,profits)):
            minHeap.append([c,p,i])
        heapq.heapify(minHeap)

        while k > 0:
            while minHeap and w >= minHeap[0][0]:
                c , p , i = heapq.heappop(minHeap)
                heapq.heappush(maxHeap,[-p,c,i])
                
            
            if maxHeap and k > 0:
                profit,cost,_ = heapq.heappop(maxHeap)
                res += -profit
                w += -profit
                
            k -= 1

        return init + res
