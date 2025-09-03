# Sudoku Solver using Backtracking

N = 9

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col, num):
    # Check row
    for x in range(N):
        if board[row][x] == num:
            return False
    
    # Check column
    for x in range(N):
        if board[x][col] == num:
            return False
    
    # Check 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board, row=0, col=0):
    if row == N - 1 and col == N:
        return True
    if col == N:
        row += 1
        col = 0
    if board[row][col] != 0:
        return solve_sudoku(board, row, col + 1)
    
    for num in range(1, N + 1):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board, row, col + 1):
                return True
        board[row][col] = 0
    return False


# Example Sudoku Puzzle (0 means empty cell)
sudoku_board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 0, 0, 0, 6, 8],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists")
