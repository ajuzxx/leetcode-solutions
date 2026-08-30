class Solution(object):
    
    def isSafeToPlace(self, board, row, col):
        #vertical check
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # left diagonal check
        i = row-1
        j = col -1

        while i>=0 and  j>=0:
            if board[i][j] == 'Q':
                return False 
            i -=1
            j -=1

        i = row -1
        j = col + 1

        while i>=0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -=1
            j += 1
        
        return True
    def nQueenHelper(self, board, ans, row):
        if row == len(board):
            solution = []
            for raw in board:
                solution.append("".join(raw))
            ans.append(solution)
            return
        for col in range(len(board)):
            if self.isSafeToPlace( board, row, col):
                board[row][col] = 'Q'
                self.nQueenHelper(board,ans,row+1)
                board[row][col] = '.'
    def solveNQueens(self,n):
        board=[['.'for _ in range(n)] for _ in range(n)]
        ans = []
        self.nQueenHelper(board, ans, 0)
        return ans



        

                

