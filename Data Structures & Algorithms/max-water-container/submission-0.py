class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            ar = (r - l) * min(heights[l], heights[r])
            maxAr = max(ar, maxAr)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAr
        