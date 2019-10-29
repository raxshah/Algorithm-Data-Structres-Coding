import copy
from collections import defaultdict
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_valid(i,j):            
            if row[i] != 0 or col[j] != 0:
                return False
            
            result = True
            if i == j:
                result = diag[0]
            if result and i + j == n-1:
                result = diag[1]
            
            return result

        def update_board(i,j):
            row[i] += 1
            col[j] += 1
            if i == j:
                diag[0] = False
            if i + j == n-1:
                diag[1] = False
        
        def remove_board(i,j):
            row[i] -= 1
            col[j] -= 1
            if i == j:
                diag[0] = True
            if i + j == n-1:
                diag[1] = True            
        
        def helper(rem_q, i):

            #base cases
            if  i == n:
                if rem_q == 0 or rem_q == -1:
                    result.append(["".join(row) for row in copy.deepcopy(board)] )                
                return 
                            
            for j in range(n):
                if is_valid(i,j):      
                    board[i][j] = 'Q'
                    update_board(i,j)
                    helper(rem_q-1, i+1)
                    board[i][j] = '.'
                    remove_board(i,j)
            return
                 
        row, col,diag = defaultdict(int), defaultdict(int), [True,True]
        result = []
        board = [["."]*n for i in range(n)]
        helper(0,0)
        return result
        
print(Solution().solveNQueens(4))
        