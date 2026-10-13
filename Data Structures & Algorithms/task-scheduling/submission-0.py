class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        for task in tasks:
            freqMap[task] = 1 + freqMap.get(task, 0)
        
        maxHeap = [-freq for freq in freqMap.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                freq = heapq.heappop(maxHeap) + 1
                if freq:
                    q.append([freq, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time 
        