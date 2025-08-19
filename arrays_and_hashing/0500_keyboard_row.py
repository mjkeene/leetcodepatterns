class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_map = {}
        for c in 'qwertyuiop':
            row_map[c] = 1
        for c in 'asdfghjkl':
            row_map[c] = 2
        for c in 'zxcvbnm':
            row_map[c] = 3

        res = []
        for word in words:
            word_lower = word.lower()
            # if set length is > 1, chars are from different rows
            if len({row_map[c] for c in word_lower}) == 1:
                res.append(word)

        return res
