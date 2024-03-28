# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789')
        new_s = ''.join([c for c in s.lower() if c in valid_chars])

        # two pointers
        return all([new_s[i] == new_s[~i] for i in range(len(new_s))])
