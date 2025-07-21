from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        res = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            mapping[sorted_word].append(word)

        for key, value in mapping.items():
            res.append(value)

        return res
    