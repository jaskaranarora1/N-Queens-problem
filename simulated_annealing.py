import random
import math
import time
import tracemalloc


def generate_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]


def count_conflicts(board):

    n = len(board)

    cols = [0] * n
    diag1 = [0] * (2 * n)
    diag2 = [0] * (2 * n)

    for row in range(n):

        col = board[row]

        cols[col] += 1
        diag1[row - col + n] += 1
        diag2[row + col] += 1

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


def simulated_annealing(
    n,
    initial_temp=100,
    cooling_rate=0.9995,
    max_steps=500000,
    restart_limit=5
):

    best_board = None
    best_conflicts = float("inf")

    for _ in range(restart_limit):

        board = generate_board(n)

        current_conflicts = count_conflicts(board)

        temperature = initial_temp * n

        for _ in range(max_steps):

            if current_conflicts == 0:
                return board

            row = random.randint(0, n - 1)

            current_col = board[row]

            new_col = random.randint(0, n - 1)

            while new_col == current_col:
                new_col = random.randint(0, n - 1)

            board[row] = new_col

            new_conflicts = count_conflicts(board)

            delta = new_conflicts - current_conflicts

            if delta < 0:
                current_conflicts = new_conflicts

            else:

                probability = math.exp(-delta / temperature)

                if random.random() < probability:
                    current_conflicts = new_conflicts
                else:
                    board[row] = current_col

            if current_conflicts < best_conflicts:
                best_conflicts = current_conflicts
                best_board = board[:]

            temperature *= cooling_rate

            if temperature < 0.001:
                break

    return best_board


def run_test(n):

    tracemalloc.start()

    start_time = time.time()

    solution = simulated_annealing(n)

    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    print(f"N = {n}")
    print(f"Conflicts = {count_conflicts(solution)}")
    print(f"Execution Time = {end_time - start_time:.4f} seconds")
    print(f"Peak Memory Used = {peak / 1024 / 1024:.4f} MB")


if __name__ == "__main__":

    test_cases = [10, 30, 50, 100, 200, 500]

    for n in test_cases:

        print("\n----------------------")

        run_test(n)