"""
EXPERIMENT 6 — N-QUEENS PROBLEM
Source: 22IT702 LAB MANUAL (Pages 12–13)
Note: Implemented procedurally without 'def'
"""

n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

# queen_rows[col] stores the row position of queen in that column
queen_rows = [-1] * n
col = 0
solved = False

while 0 <= col < n:
    # Try the next row in the current column
    start_row = queen_rows[col] + 1

    # If a queen was previously placed in this column, remove it from the board
    if queen_rows[col] != -1:
        board[queen_rows[col]][col] = 0
        queen_rows[col] = -1

    placed = False
    for row in range(start_row, n):
        safe = True

        # 1. Check this row on the left side
        for c in range(col):
            if board[row][c] == 1:
                safe = False
                break

        if safe:
            # 2. Check upper-left diagonal
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 1:
                    safe = False
                    break
                r -= 1
                c -= 1

        if safe:
            # 3. Check lower-left diagonal
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == 1:
                    safe = False
                    break
                r += 1
                c -= 1

        if safe:
            board[row][col] = 1
            queen_rows[col] = row
            placed = True
            break

    if placed:
        if col == n - 1:
            solved = True
            break
        col += 1
    else:
        # Backtrack: reset position and move to previous column
        queen_rows[col] = -1
        col -= 1

if solved:
    print("Solution for", n, "Queens:")
    for row in board:
        print(row)
else:
    print("No solution exists")
