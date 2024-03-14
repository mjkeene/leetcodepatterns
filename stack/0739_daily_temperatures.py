# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

        # for idx, temp in enumerate(temperatures):
        #     if not stack or temp < stack[-1][0]:
        #         stack.append((temp, idx))
        #     else:
        #         while stack and stack[-1][0] < temp:
        #             days = idx - stack[-1][1]
        #             res[stack[-1][1]] = days
        #             stack.pop()
        #         stack.append((temp, idx))
        # return res
