class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # O(n) time, O(1) space
        min1, min2 = float("inf"), float("inf")

        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
        leftover = money - (min1 + min2)
        return leftover if leftover >= 0 else money


        # O(n log n) due to sort
        # prices.sort()
        # if money - (prices[0] + prices[1]) >= 0:
        #     return money - (prices[0] + prices[1])
        # else:
        #     return money
    