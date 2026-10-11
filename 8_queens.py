N = 8                                      # board size and number of queens

def print_solution(board):                 # display a board
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))   # Q = queen, . = empty
    print()

def is_safe(board, row, col):              # can a queen go at (row, col)?
    for i in range(col):                   # same row, to the left
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):    # upper-left diagonal
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):         # lower-left diagonal
        if board[i][j] == 1:
            return False
    return True                            # no attacks found

count = 0                                  # number of solutions found
first = None                               # copy of the first solution

def solve(board, col):
    global count, first
    if col >= N:                           # all 8 columns filled, so it is a solution
        count += 1
        if first is None:
            first = [row[:] for row in board]   # save a copy of the first one
        return
    for row in range(N):                   # try every row in this column
        if is_safe(board, row, col):
            board[row][col] = 1            # place queen
            solve(board, col + 1)          # move to the next column
            board[row][col] = 0            # BACKTRACK: remove the queen

board = [[0] * N for _ in range(N)]        # empty 8x8 board
solve(board, 0)                            # start from column 0
print("First solution:")
print_solution(first)
print("Total solutions:", count)