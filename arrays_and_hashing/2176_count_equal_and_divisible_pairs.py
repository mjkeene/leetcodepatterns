from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # This approach only compares indices of equal elements
        value_indices = defaultdict(list)
        count = 0

        # Save time, use extra space to group indices by value
        for idx, val in enumerate(nums):
            value_indices[val].append(idx)

        # For each group of same values, check the indices
        for _, indices in value_indices.items():
            n = len(indices)
            for i in range(n):
                for j in range(i+1, n):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count

        # # O(n^2) approach
        # count = 0
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j] and (i * j) % k == 0:
        #             count += 1
        # return count
