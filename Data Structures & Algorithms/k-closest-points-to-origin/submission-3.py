class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        res = []

        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(max_heap, (-dist, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        for _ in range(k):
            dist, x, y = heapq.heappop(max_heap)
            res.append([x, y])
            k -= 1

        return res

            