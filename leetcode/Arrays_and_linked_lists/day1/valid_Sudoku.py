"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


507 / 507 test cases passed.
Status: Accepted
Runtime: 100 ms
Memory Usage: 14.4 MB
Submitted: 1 minute ago

Runtime: 96 ms, faster than 69.72% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14.1 MB, less than 96.72% of Python3 online submissions for Valid Sudoku.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_rows(board)  and self.check_3x3(board) and self.check_cols(board)
        
    def check_rows(self, board):
        for row in board:
            check = [i for i in row if i != '.']
            if len(set(check)) != len(check):
                return False
        return True
    
    def check_cols(self, board):
        for i in range(0,len(board)):
            list1 = list()
            set1 = set()
            for j in range(0,len(board[0])):
                if board[j][i] == ".":
                    continue
                list1.append(board[j][i])
                set1.add(board[j][i])
            if len(list1) != len(set1):
                return False
        return True
    
    def check_3x3(self, board):
        sections = [ 9, 6, 3, 0 ]
        check = list()
        for k in range(3, 0, -1):
            for i in range(0, 9):
                for j in range(sections[k], sections[k-1]):
                    check.append(board[i][j])
        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i + n]
        squres = list(chunks(check,9))
        for i in squres:
            check_squres = [i for i in i if i != '.']
            if len(set(check_squres)) != len(check_squres):
                return False
        return True


"""
better sol with hashtable
Runtime: 88 ms, faster than 95.02% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14 MB, less than 96.72% of Python3 online submissions for Valid Sudoku.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isSubBox(i,j,x,y):
            if (i//3 == x//3) and (j//3 == y//3):
                return True
            return False
            
        hashtable = {}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num not in hashtable.keys():
                        hashtable[num] = [(i,j)]
                    else:
                        for (x,y) in hashtable[num]:
                            if x == i or y == j or isSubBox(i,j,x,y):
                                return False
                        hashtable[num] += [(i,j)]
        return True
                      