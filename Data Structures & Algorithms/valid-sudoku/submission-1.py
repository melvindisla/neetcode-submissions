class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        
        # keep in mind the sudoku boards are a fixed sized, so we use the following
        for r in range(9):
            for c in range(9):
                
                # check if the index is "empty"
                if board[r][c] == ".":
                    continue
                # check if the element is in the map
                if (
                    board[r][c] in rows[r] or 
                    board[r][c] in columns[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                # Add the element the corresponding maps
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True