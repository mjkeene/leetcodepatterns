# https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # one liner using built-in sorted func
        # return sorted(s) == sorted(t)

        if not len(s) == len(t):
            return False

        # frequency mappings for letter counts in each word
        d1, d2 = {}, {}
        for i in range(len(s)):
            d1.setdefault(s[i], 0)
            d1[s[i]] += 1
            d2.setdefault(t[i], 0)
            d2[t[i]] += 1
        return d1 == d2
