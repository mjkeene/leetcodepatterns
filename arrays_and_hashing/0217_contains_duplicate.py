# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            d.setdefault(num, 0)
            d[num] += 1
            if d[num] > 1:
                return True
        return False

        # return not len(nums) == len(set(nums))

        # sort, iterate through comparing items next to each other
        # nums = [1,2,3,1] -> [1, 2, 2, 3]
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
