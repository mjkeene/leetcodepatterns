# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}
        # if s is odd number, return false
        if len(s) % 2 != 0:
            return False

        # add open brackets to stack, when retrieving closed bracket, it must match closing
        for char in s:
            if char in mapping.keys():
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif mapping[stack.pop()] != char:
                return False
        return not stack
    