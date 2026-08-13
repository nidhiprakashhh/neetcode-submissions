class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True

        s = s.lower()

        leftPtr = 0
        rightPtr = len(s) - 1

        while leftPtr < rightPtr:
            while leftPtr < rightPtr and not s[leftPtr].isalnum():
                leftPtr += 1
            while rightPtr > leftPtr and not s[rightPtr].isalnum():
                rightPtr -= 1

            if s[leftPtr] != s[rightPtr]:
                return False

            leftPtr += 1
            rightPtr -= 1

        return True
        