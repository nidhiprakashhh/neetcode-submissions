class Solution:
    def isValid(self, s: str) -> bool:

        opening = "([{"
        closing = ")]}"

        pairs = {")" : "(", "]" : "[" , "}" : "{"}

        stack = []

        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
        