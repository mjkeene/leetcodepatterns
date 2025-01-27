class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # note that greedy approach does not work for this
        # sort so that we can break if amount - coin is negative
        coins.sort()

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amount in range(1, amount + 1):
            for coin in coins:
                diff = amount - coin
                if diff < 0:
                    break
                dp[amount] = min(dp[amount], dp[diff] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
    