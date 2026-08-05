class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        l = len(nums)

        if l == 0 or l == 1:
            return False

        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                return True
        
        return False