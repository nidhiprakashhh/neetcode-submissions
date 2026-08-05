class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        l = len(nums)

        if l == 0 or l == 1:
            return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False