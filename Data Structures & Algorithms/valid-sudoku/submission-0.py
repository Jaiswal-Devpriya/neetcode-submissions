class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                value = board[row][col]

                
                if value == ".":
                    continue

                
                for other_col in range(9):
                    if other_col != col and board[row][other_col] == value:
                        return False

               
                for other_row in range(9):
                    if other_row != row and board[other_row][col] == value:
                        return False

                box_start_row = (row // 3) * 3
                box_start_col = (col // 3) * 3

                for box_row in range(box_start_row, box_start_row + 3):
                    for box_col in range(box_start_col, box_start_col + 3):
                        if (
                            (box_row != row or box_col != col)
                            and board[box_row][box_col] == value
                        ):
                            return False

        return True
        