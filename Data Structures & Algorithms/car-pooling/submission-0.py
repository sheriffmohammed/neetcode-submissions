class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        hashmap = {}
        max_len = passengers = 0
        
        for _, _, to in trips:
            max_len = max(max_len,to)+1
        arr = [0 for i in range(max_len)]
        
        for n, f, t in trips:
            if arr[f]:
                arr[f][0] += n
                hashmap[t] = hashmap.get(t,0) + n 
                continue
            arr[f] =  [n,f,t]
            hashmap[t] = hashmap.get(t,0) + n 

        for i in range(len(arr)):
            passengers -= hashmap.get(i,0)
            if arr[i]:
                n,f,t = arr[i]
            else:
                continue   
            passengers += n
            if passengers > capacity:
                return False
            
        return True        
                