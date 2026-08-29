class Solution:
    def isValid(self, s: str) -> bool:

        opening = "([{"
        closing = ")]}"

        pairs = {")" : "(", "]" : "[" , "}" : "{"}

        stack = []

        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif s[i] in closing:
                if len(stack) == 0 or stack[-1] != pairs[s[i]]:
                    return False
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False
        