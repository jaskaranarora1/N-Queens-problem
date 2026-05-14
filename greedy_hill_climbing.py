import random
import time
import tracemalloc


def initialize_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]


def compute_conflicts(board):

    n = len(board)

    cols = [0] * n
    diag1 = [0] * (2 * n)
    diag2 = [0] * (2 * n)

    for row in range(n):
        col = board[row]

        cols[col] += 1
        diag1[row - col + n] += 1
        diag2[row + col] += 1

    return cols, diag1, diag2


def total_conflicts(board):

    n = len(board)

    cols, diag1, diag2 = compute_conflicts(board)

    conflicts = 0

    for row in range(n):
        col = board[row]

        conflicts += (
            cols[col]
            + diag1[row - col + n]
            + diag2[row + col]
            - 3
        )

    return conflicts // 2


def conflicted_rows(board):

    n = len(board)

    cols, diag1, diag2 = compute_conflicts(board)

    rows = []

    for row in range(n):
        col = board[row]

        conflicts = (
            cols[col]
            + diag1[row - col + n]
            + diag2[row + col]
            - 3
        )

        if conflicts > 0:
            rows.append(row)

    return rows


def min_conflicts(n, max_steps=100000):

    board = initialize_board(n)

    for _ in range(max_steps):

        if total_conflicts(board) == 0:
            return board

        row = random.choice(conflicted_rows(board))

        best_col = board[row]
        min_conflict = float("inf")

        for col in range(n):

            original = board[row]
            board[row] = col

            conflicts = total_conflicts(board)

            if conflicts < min_conflict:
                min_conflict = conflicts
                best_col = col

            board[row] = original

        board[row] = best_col

    return board


def run_test(n):

    tracemalloc.start()

    start_time = time.time()

    solution = min_conflicts(n)

    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    print(f"N = {n}")
    print(f"Conflicts = {total_conflicts(solution)}")
    print(f"Execution Time = {end_time - start_time:.4f} seconds")
    print(f"Peak Memory Used = {peak / 1024 / 1024:.4f} MB")


if __name__ == "__main__":

    test_cases = [10, 30, 50, 100, 200, 500]

    for n in test_cases:

        print("\n----------------------")

        if n > 100:

            print(f"N = {n}")
            print("Skipped: Runtime too high for Greedy Hill Climbing")

            continue

        run_test(n)