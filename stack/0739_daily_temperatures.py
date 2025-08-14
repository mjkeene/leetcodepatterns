# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                popped = stack.pop()
                num_days = idx - popped[0]
                res[popped[0]] = num_days
            stack.append((idx, temp))

        return res
