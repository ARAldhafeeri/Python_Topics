def check_3x3(board):
    sections = [ 9, 6, 3, 0 ]
    check = list()
    for k in range(3, 0, -1):
        for i in range(0, 9):
            for j in range(sections[k], sections[k-1]):
                check.append(board[i][j])
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    squres = list(chunks(check,9))
    print(squres)
    for i in squres:
        list1 = list()
        set1 = set()
        for j in i:
            if j == ".":
              continue
            list1.append(j)
            set1.add(j)
        print(list1, set1)
        if len(set1) != len(list1):
          return False
    return True




board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(check_cols(board))