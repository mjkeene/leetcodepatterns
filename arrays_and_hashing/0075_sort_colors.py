class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort
        count = [0] * 3
        for index in nums:
            count[index] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1
        return nums
    