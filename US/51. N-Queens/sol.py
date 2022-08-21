
# https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for j in range(n)] for i in range(n)]
        self.ret = []
        self.nQueen(board, 0)
        return self.ret
        
    def nQueen(self, board, row):
        n = len(board)
        for col in range(n):
            if self.isValid(board, row, col):
                board[row][col] = 'Q'
                if row == n-1:
                    self.addRet(board)
                    board[row][col] = '.'
                    return
                self.nQueen(board, row+1)
                board[row][col] = '.'
                
       
    def isValid(self, board, r, c):
        n = len(board)
        for i in range(n):
            if board[i][c] == 'Q':
                return False
        tmprow, tmpcol = r-1, c-1
        while tmprow>=0 and tmpcol >= 0:
            if board[tmprow][tmpcol] == 'Q':
                return False
            tmprow -= 1
            tmpcol -= 1
        tmprow, tmpcol = r-1, c+1
        while tmprow>=0 and tmpcol <= n-1:
            if board[tmprow][tmpcol] == 'Q':
                return False
            tmprow -= 1
            tmpcol += 1
        return True
                
    def addRet(self, board):
        tmp = []
        for row in board:
            s = "".join(row)
            tmp.append(s)
        self.ret.append(tmp)
            
    
