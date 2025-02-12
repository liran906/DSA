# Valid Sudoku
# https://neetcode.io/problems/valid-sudoku
# m

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            if not self.noDupe(board[i]):
                return False
            
        # check collum
        for i in range(9):
            if not self.noDupe([row[i] for row in board]):
                return False
            
        # check block
        for sr in (0, 3, 6):
            for sc in (0, 3, 6):
                toCheck = []
                for r in range(3):
                    for c in range(3):
                        toCheck.append(board[sr+r][sc+c])
                if not self.noDupe(toCheck):
                    return False
        return True
    
    def noDupe(self, lst):
        check = [0] * 9
        for i in lst:
            if i == '.':
                continue
            i = int(i)
            if check[i-1] == 1:
                return False
            check[i-1] += 1
        return True