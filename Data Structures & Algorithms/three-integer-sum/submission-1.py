class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, e in enumerate(nums):
            if i > 0 and e == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[l] + nums[r] + e

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([e, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

        


        