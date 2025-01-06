class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 1. Iterate through asteroids from left to right
        # 2. For each asteroid, check direction:
        # - If it is moving right (positive), add it to the stack
        # - If it is moving left (negative), handle collisions with asteroids in stack
        # Return stack with remaining asteroids
        stack = []

        for val in asteroids:
            # Check for potential collisions
            while stack and val < 0 < stack[-1]:
                # Top asteroid is larger, current asteroid explodes
                if abs(stack[-1]) > abs(val):
                    break
                # Top asteroid is smaller, pop it from stack
                elif abs(stack[-1]) < abs(val):
                    stack.pop()
                    continue
                # Both are same size, both explode
                else:
                    stack.pop()
                    break
            # Note that this else block has no "if" statement, it is attached to the
            # "while" loop. "For" loops can also have else clauses. This block is only
            # executed if the while loop completes normally (without breaking).
            else:
                # No collision, append asteroid val to stack
                stack.append(val)

        return stack
