class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [[-v,k,0] for k,v in count.items()]
        heapq.heapify(maxHeap)
        res = []
        q = deque([])
        timer = 0

        while maxHeap or q:
            if q and q[0][2] < timer:
                val , char , time = q.popleft()
                heapq.heappush(maxHeap,[val,char,time])
            
            if maxHeap:
                v , c , t = heapq.heappop(maxHeap)
                res.append(c)
                q.append([v+1,c,timer+n]) if v+1 < 0 else None
            else:
                res.append(None)
            timer +=1
        return len(res)  