class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0

        for i in range(len(nums)):
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + nums[i])

            if i >= len(nums) - 1:
                return True

        return False

        # Invert -- start from last index, see if you can reach beginning
        # Shift the goal if you can reach certain indices, iterating backwards
        # goal = len(nums) - 1

        # for i in range(len(nums) - 1, -1, -1):
        #     print(i, nums[i], goal)
        #     # If index + value >= goal, we can reach that index, so make that the new goal
        #     # Continue this all the way to index 0 to see if we can reach beginning
        #     if i + nums[i] >= goal:
        #         goal = i

        # return goal == 0