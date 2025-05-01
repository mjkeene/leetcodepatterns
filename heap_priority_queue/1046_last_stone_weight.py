import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use Python's min heap (heapq) to pop max items in O(log n) time
        heap_vals = [-w for w in stones]
        heapq.heapify(heap_vals)

        while len(heap_vals) > 1:
            first = heapq.heappop(heap_vals) * -1
            second = heapq.heappop(heap_vals) * -1
            if first > second:
                heapq.heappush(heap_vals, (first - second) * -1)

        if not heap_vals:
            return 0

        return heapq.heappop(heap_vals) * -1
    