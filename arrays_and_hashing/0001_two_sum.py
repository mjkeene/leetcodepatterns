# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for idx, item in enumerate(nums):
            diff = target - item
            if diff in mapping:
                return [mapping[diff], idx]
            mapping[item] = idx

        # O(n^2), reasonably efficient on "small" nums array
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
