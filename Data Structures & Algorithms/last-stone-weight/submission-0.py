class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heavy1 = heapq.heappop(stones)
            heavy2 = heapq.heappop(stones)
            if (heavy2 > heavy1):
                heapq.heappush(stones, heavy1 - heavy2)

        heapq.heappush(stones, 0)
        return abs(stones[0])


        