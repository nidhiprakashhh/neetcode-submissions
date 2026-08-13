class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        leftPtr = 0
        rightPtr = len(numbers) - 1

        while leftPtr < rightPtr:
            add = numbers[leftPtr] + numbers[rightPtr]
            if add == target:
                return [leftPtr + 1, rightPtr +1]
            if add > target:
                rightPtr -= 1
            else:
                leftPtr += 1

        
        