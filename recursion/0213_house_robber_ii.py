class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, A):
        # Do calculations here, rob logic
        if len(A) == 1:
            return A[0]

        res = []
        res.append(A[0])
        res.append(max(A[0], A[1]))

        for i in range(2, len(A)):
            max_val = max(A[i] + res[i - 2], res[i - 1])
            res.append(max_val)

        # print(res)
        return res[-1]