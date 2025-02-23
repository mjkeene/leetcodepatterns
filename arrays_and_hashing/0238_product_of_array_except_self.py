class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Compute prefix and postfix values upfront, use those to determine result
        res = []
        prefix = [nums[0]]
        postfix = [nums[-1]]

        for i in range(1, len(nums)):
            curr_num_pre = prefix[i-1] * nums[i]
            curr_num_post = postfix[i-1] * nums[~i]
            prefix.append(curr_num_pre)
            postfix.append(curr_num_post)
        # Postfix needs to be reversed since we iterated forwards over nums array
        postfix = postfix[::-1]

        # Loop over nums, use prefix and postfix to calculate final value
        # ith element -> multiply pre[i-1] * post[i+1]
        # Load first and last items independently to avoid index issues
        res.append(postfix[1])
        for i in range(1, len(nums)-1):
            res.append(prefix[i-1] * postfix[i+1])
        res.append(prefix[-2])

        return res

        # # O(n^2) implementation
        # res = []
        # for i in range(len(nums)):
        #     curr_num = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         curr_num = curr_num * nums[j]
        #     res.append(curr_num)
        # return res
