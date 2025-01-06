class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        return ' '.join(split[::-1])