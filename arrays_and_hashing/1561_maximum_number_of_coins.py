class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        total = 0
        piles.sort()

        for i in range(len(piles) // 3):
            piles.pop()
            total += piles.pop()
            del piles[0]

        return total
