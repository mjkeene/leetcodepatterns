class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == '*': # stack can't be empty, so don't need to check
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
