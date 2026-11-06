class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1 #n = 5 [8,5,3,2,1,1]
                #      [0,1,2,3,4,5]

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

        