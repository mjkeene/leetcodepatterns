class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter.setdefault(n, 0)
            counter[n] += 1

        tuples = []
        for num, count in counter.items():
            tuples.append((num, count))

        tuples.sort(key=lambda x: x[1], reverse=True)
        res = [tuples[i][0] for i in range(k)]

        return res