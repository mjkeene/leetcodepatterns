class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                curr_val = board[row][col]
                # represents empty sub-box
                if curr_val == '.':
                    continue
                # duplicate detected
                if (curr_val in row_map[row] or
                    curr_val in col_map[col] or
                    curr_val in square_map[(row // 3, col // 3)]):
                    return False
                # update mappings
                row_map[row].add(curr_val)
                col_map[col].add(curr_val)
                square_map[(row // 3, col // 3)].add(curr_val)
            
        return True
