class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 1]
        for i in range(2, n + 1):
            steps.append(steps[i - 2] + steps[i - 1])

        return steps[n]

        if n == 0:
            return 1
        elif n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
