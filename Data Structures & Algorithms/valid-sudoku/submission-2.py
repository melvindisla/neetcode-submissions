class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set) # {1:{1,2,3,4,5}}
        cols = defaultdict(set)
        squares = defaultdict(set) # {(0,0): {1,2,4,8,9}
                                   #  (0,1):{3,5}   }


        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                elif ( board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3 , c //3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r //3 , c //3)].add(board[r][c])
        return True