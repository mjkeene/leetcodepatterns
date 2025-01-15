class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # normalize k to avoid duplicate work if k > len(nums)
        k = k % len(nums)
        res = nums[-k:] + nums[:-k]
        nums[:] = res

        # O(1) extra space, inefficient with inserting at 0th index though --
        # This is an O(n) operation done k times, O(k*n), so if k is close to n,
        # this can become O(n^2)
        # k = k % len(nums)
        # for i in range(k):
        #     n = nums.pop()
        #     nums.insert(0, n)
