
def notInRow(num,row,board):
    '''
    Checks if the digit is already in the same row.

    Argument(s):
    num: the digit attempting to be inserted
    row: the row the number is attempting to be inserted in
    board: 2D sudoku array

    Return(s):
    validRow: True if the row is valid for the digit to be inserted in,
    False otherwise
    '''
    validRow = True
    for i in board[row]:
        if i == num:
            validRow = False
    return validRow

def notInColumn(num,col,board):
    '''
    Checks if the digit is already in the same column.

    Argument(s):
    num: the digit attempting to be inserted
    col: the column the number is attempting to be inserted in
    board: 2D sudoku array

    Return(s):
    validCol: True if the column is valid for the digit to be inserted in,
    False otherwise
    '''
    validCol = True
    for i in board:
        if i[col] == num:
            validCol = False
    return validCol

def notInBlock(num,row,col,board):
    '''
    Checks if the digit is already in the same sub-grid.

    Argument(s):
    num: the digit attempting to be inserted
    row: the row the number is attempting to be inserted in
    col: the column the number is attempting to be inserted in
    board: 2D sudoku array

    Return(s):
    validCol: True if the sub-grid is valid for the digit to be inserted in,
    False otherwise
    '''
    validBlock = True
    start1 = row // 3
    start2 = col // 3
    for i in range(start1*3, start1*3 + 3):
        for j in range(start2*3, start2*3 + 3):
            if board[i][j] == num:
                validBlock = False
    return validBlock

def isComplete(board):
    '''
    Checks if the sudoku board is full of digits.

    Argument(s):
    board: 2D sudoku array
    '''
    full = True
    for i in board:
        for j in i:
            if j == 0:
                full = False
    return full

def nextEmpty(board):
    '''
    Searches the 2D sudoku array for the next empty space. 
    '''
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return row,col
    return None

def valid(num,row,col,board):
    '''
    Checks if the digit is safe to be placed in the selected location

    Argument(s):
    num: the digit attempting to be inserted
    row: the row the number is attempting to be inserted in
    col: the column the number is attempting to be inserted in
    board: 2D sudoku array

    Return(s):
    True if digit can be placed safely. False otherwise.
    '''
    return notInRow(num,row,board) and notInColumn(num,col,board) and notInBlock(num,row,col,board)

def solve(board):
    '''
    Recursively solves the sudoku puzzle.

    Argument(s):
    board: the 2D sudoku array to be solved.
    '''
    if isComplete(board):
        return True
    else:
        row, col = nextEmpty(board)

        for i in range(1,10):

            if valid(i,row,col,board):
                board[row][col] = i

                if solve(board):
                    return True 
                else:
                    board[row][col] = 0