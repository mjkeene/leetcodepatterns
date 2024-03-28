# https://leetcode.com/problems/binary-search/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 20 iterations to search array of size 1M (O(log(n)))
        # for loop -> 1M iterations to search arrray of size 1M (O(n))
        def bin_search_recursive(arr, target, low, high):
            if low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    return bin_search_recursive(arr, target, low, mid - 1)
                else:
                    return bin_search_recursive(arr, target, mid + 1, high)
            else:
                return -1
        return bin_search_recursive(nums, target, 0, len(nums)-1)

        # def bin_search_iter(arr, target):
        #     l, r = 0, len(arr) - 1
        #     while l <= r:
        #         m = (l + r) // 2
        #         if arr[m] == target:
        #             return m
        #         elif arr[m] > target:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     return -1
        # return bin_search_iter(nums, target)