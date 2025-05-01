import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)

        val = 0
        for _ in range(k):
            val = heapq.heappop(heap)

        return val * -1

        # # heapq builtin to find kth
        # return heapq.nlargest(k, nums)[-1]

        # # sorting, easy
        # nums.sort(reverse=True)
        # return nums[k-1]
