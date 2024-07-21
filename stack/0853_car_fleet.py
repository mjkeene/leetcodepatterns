class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # only 1 car, must be only 1 fleet
        if len(position) == 1:
            return 1

        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(key=lambda x : x[0], reverse=True)

        for p, s in pairs:
            stack.append((target - p) / s)
            # if stack[-1] <= stack[-2], then they become a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
