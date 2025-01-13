# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                curr_item = stack.pop()
                curr_index = curr_item[0]
                res[curr_index] = idx - curr_index
            stack.append((idx, temp))
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
