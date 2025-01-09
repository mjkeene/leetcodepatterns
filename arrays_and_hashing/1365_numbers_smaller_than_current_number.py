class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: Sort the array (copy, still need original ordering for final solution)
        sorted_nums = sorted(nums)

        # Step 2: Create mapping using array indices
        mapping = {}
        for idx, num in enumerate(sorted_nums):
            if num not in mapping:
                mapping[num] = idx

        # Step 3: Create result array based on mapping indices
        res = [mapping[num] for num in nums]
        return res

        # O(n^2) with nested loop solution
        #
        # res = []
        # for i in range(len(nums)):
        #     main_num = nums[i]
        #     count = 0
        #     for j in range(len(nums)):
        #         curr_num = nums[j]
        #         if curr_num < main_num:
        #             count += 1
        #     res.append(count)
        # return res
