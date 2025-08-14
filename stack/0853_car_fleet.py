class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # group based on how many iterations (units of time) will it take to arrive at target
        stack, pairs = [], []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort(key=lambda x: x[0], reverse=True)

        for item in pairs:
            time = (target - item[0]) / item[1]
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
        