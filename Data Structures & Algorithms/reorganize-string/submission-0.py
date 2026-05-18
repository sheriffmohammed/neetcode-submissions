class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-v,k] for k ,v in count.items()]
        heapq.heapify(maxHeap)
        prev_v , prev_c = 0, ""
        res = []

        while maxHeap:
            v,c = heapq.heappop(maxHeap)
            res.append(c)
            if prev_v < 0:
                heapq.heappush(maxHeap,[prev_v,prev_c])
            
            prev_v , prev_c = v+1 , c

        return "".join(res) if len(res) == len(s) else ""