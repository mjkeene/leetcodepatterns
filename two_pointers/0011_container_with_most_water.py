class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            distance = r - l
            area = distance * min_height
            max_area = max(area, max_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
