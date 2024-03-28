import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max(piles) is the eating speed (k) if len(piles) == num hours (h)
        if len(piles) == h:
            return max(piles)

        # use binary search within the solution set (1, ..., max(piles))
        l, r = 1, max(piles)
        min_eating_speed = r

        # verify if eating speed works, update min value
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                min_eating_speed = min(k, min_eating_speed)
                r = k - 1
            else:
                l = k + 1

        return min_eating_speed
