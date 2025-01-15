class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings_split = s.split()
        return len(strings_split[-1])