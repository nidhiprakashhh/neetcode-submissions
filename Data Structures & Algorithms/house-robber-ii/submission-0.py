class Solution:
    def rob(self, nums: List[int]) -> int:

        def linearRob(nums):
            rob1 = 0
            rob2 = 0
            for i in range(len(nums)):
                nums[i] = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = nums[i]

            return rob2
        
        if len(nums) == 1:
            return nums[0]
        else:
            return max(linearRob(nums[1:]),
            linearRob(nums[:len(nums) - 1]))

        