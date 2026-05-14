import time
import psutil
import os


def is_safe(board, row, col):

    for prev_row in range(row):

        prev_col = board[prev_row]

        # Same column
        if prev_col == col:
            return False

        # Same diagonal
        if abs(prev_col - col) == abs(prev_row - row):
            return False

    return True


def solve_dfs(n):

    board = [-1] * n

    def backtrack(row):

        if row == n:
            return True

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                if backtrack(row + 1):
                    return True

                board[row] = -1

        return False

    if backtrack(0):
        return board

    return None


def count_conflicts(board):

    if board is None:
        return -1

    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):

            # Same column
            if board[i] == board[j]:
                conflicts += 1

            # Same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def run_test(n):

    process = psutil.Process(os.getpid())

    start_memory = process.memory_info().rss / 1024 / 1024
    start_time = time.time()

    solution = solve_dfs(n)

    end_time = time.time()
    end_memory = process.memory_info().rss / 1024 / 1024

    execution_time = end_time - start_time
    memory_used = end_memory - start_memory

    print(f"N = {n}")
    print(f"Solution Found = {solution is not None}")
    print(f"Conflicts = {count_conflicts(solution)}")
    print(f"Execution Time = {execution_time:.4f} seconds")
    print(f"Memory Used = {memory_used:.4f} MB")
    print(f"Solution = {solution}")


if __name__ == "__main__":

    # DFS only feasible for small N
    run_test(10)