# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [0,1,2,4,5,6,7]
        #  |     |     |
        #  L     M     R
        # Logic:
        # L < M < R : set left as temporary min
        # [4,5,6,7,0,1,2]
        #  |     |     |
        #  L     M     R
        # L < M > R : mid is part of left sorted array, go right
        # after setting min to min(res, nums[mid])
        # [0, 1, 2]
        #  |  |  |
        #  L  M  R
        # L < M < R

        left, right = 0, len(nums) - 1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (right + left) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res
