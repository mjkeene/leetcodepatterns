class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        # iterate through num_set to avoid duplicates
        for num in num_set:
            # check for start of sequence only
            if num - 1 not in num_set:
                curr = 0
                while num + curr in num_set:
                    curr += 1
                longest = max(curr, longest)
        
        return longest
