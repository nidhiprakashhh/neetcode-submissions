class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distMap = defaultdict(list)
        res = []

        for point in points:
            dist = (point[0]**2) + (point[1]**2)
            distMap[dist].append(point)

        distHeap = []
        for dist in distMap:
            heapq.heappush(distHeap, dist)

        while k > 0:
            closest = heapq.heappop(distHeap)
            for point in distMap[closest]:
                res.append(point)
                k -= 1
                if k == 0:
                    break

        return res

            