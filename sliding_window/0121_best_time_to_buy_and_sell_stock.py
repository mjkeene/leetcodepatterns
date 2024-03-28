# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers, buy with l, sell with r
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit

        # O(n) iterative solution
        # min_so_far, max_profit = prices[0], 0
        # for i in range(1, len(prices)):
        #     if prices[i] - min_so_far > 0:
        #         max_profit = max(max_profit, prices[i] - min_so_far)
        #     if min_so_far > prices[i]:
        #         min_so_far = prices[i]
        # return max_profit
