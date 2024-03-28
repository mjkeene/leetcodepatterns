# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search_recursive(arr, low, high, target):
            if high >= low:
                mid = (high + low) // 2
                curr_row = arr[mid]

                first_num_in_row, last_num_in_row = curr_row[0], curr_row[-1]
                # target is in row to the left of curr_row
                if first_num_in_row > target:
                    return bin_search_recursive(matrix, low, mid - 1, target)

                # target is in row to the right of curr_row
                elif last_num_in_row < target:
                    return bin_search_recursive(matrix, mid + 1, high, target)

                # curr_row contains the target value if it exists
                else:
                    for num in curr_row:
                        if num == target:
                            return True
                    return False
            else:
                return False
        return bin_search_recursive(matrix, 0, len(matrix)-1, target)
"""
        def bin_search_iter(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] > target:
                    right = mid - 1
                elif arr[mid][-1] < target:
                    left = mid + 1
                else:
                    for num in arr[mid]:
                        if num == target:
                            return True
            return False
        return bin_search_iter(matrix, target)

    # O(n) solution not using binary search
    for row in matrix:
        for num in row:
            if num == target:
                return True
    return False
"""