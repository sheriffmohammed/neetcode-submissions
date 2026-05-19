class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        heapq.heapify(tasks)
        to_process = []
        time = tasks[0][0]

        while tasks or to_process:
            
            while tasks and tasks[0][0] <= time:
                et , pt , i= heapq.heappop(tasks)
                heapq.heappush(to_process,[pt,i])
            
            if not to_process:
                time = tasks[0][0]
                continue

            pt , i = heapq.heappop(to_process)
            time += pt
            res.append(i)
        return res      
