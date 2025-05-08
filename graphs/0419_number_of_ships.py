class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        def dfs(r, c):
            if board[r][c] != 'X':
                return 
            board[r][c] = '@' # visited

            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for x, y in dirs:
                dr, dc = r + x, c + y

                if 0 <= dr < ROWS and 0 <= dc < COLS and board[dr][dc] == 'X':
                    dfs(dr, dc)
        
        ROWS, COLS = len(board), len(board[0])
        num_ships = 0

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X':
                    dfs(r, c)
                    num_ships += 1
        return num_ships
        