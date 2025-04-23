class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign

        res = int(str(x)[::-1])
        res *= sign

        if res > 2**31 - 1 or res < -2**31:
            return 0

        return res
