class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            subproblems = [dp[k] for k in range(i) if nums[k] < nums[i]]
            dp[i] = 1 + max(subproblems, default=0)

        return max(dp, default=0)
