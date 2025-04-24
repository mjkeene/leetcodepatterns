class Solution:
    def climbStairs(self, n: int) -> int:
        # O(1) space tabulation (bottom up DP)
        prev, curr = 1, 1

        for i in range(n - 1):
            prev, curr = curr, prev + curr

        return curr
