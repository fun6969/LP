def solve_n_queens(n):
    def print_solution(board):
        for row in board:
            print(" ".join("Q" if col else "." for col in row))
        print()

    def solve(row):
        if row == n:
            print_solution(board)
            return

        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                board[row][col] = 1
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True

                solve(row + 1)  # Recursive call to next row

                # Backtrack
                board[row][col] = 0
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    # Initialization
    board = [[0 for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # major diagonal (\)
    diag2 = [False] * (2 * n - 1)  # minor diagonal (/)

    solve(0)

# Run the N-Queens solver for a specific N
solve_n_queens(4)
