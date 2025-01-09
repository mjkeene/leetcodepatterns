class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create mapping, iterate over strs, sort the word
        # If that key (sorted word) already exists in dict, append the original word
        # Else, initialize the key/val pair with sorted word, empty array
        # Append that unsorted word to that key's array

        mapping = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            mapping.setdefault(sorted_s, [])
            mapping[sorted_s].append(s)

        res = []
        for k, v in mapping.items():
            res.append(v)

        return res