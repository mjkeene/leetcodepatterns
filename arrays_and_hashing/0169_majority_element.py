class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        # Other candidates cannot "outvote" the majority element

        candidate, count = None, 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

        ## Basic approach with freq dictionary
        # freq = {}

        # for n in nums:
        #     freq.setdefault(n, 0)
        #     freq[n] += 1

        # for k, v in freq.items():
        #     if v > (len(nums) / 2):
        #         return k
