import random
import time
import tracemalloc


POPULATION_SIZE = 200
GENERATIONS = 3000
MUTATION_RATE = 0.15
ELITE_SIZE = 20


def generate_board(n):

    board = list(range(n))

    random.shuffle(board)

    return board


def count_conflicts(board):

    n = len(board)

    conflicts = 0

    diag1 = {}
    diag2 = {}

    for row in range(n):

        col = board[row]

        d1 = row - col
        d2 = row + col

        diag1[d1] = diag1.get(d1, 0) + 1
        diag2[d2] = diag2.get(d2, 0) + 1

    for diag in [diag1, diag2]:

        for count in diag.values():

            if count > 1:
                conflicts += count * (count - 1) // 2

    return conflicts


def fitness(board):

    return -count_conflicts(board)


def selection(population):

    population.sort(key=fitness, reverse=True)

    return population[:POPULATION_SIZE // 2]


def crossover(parent1, parent2):

    n = len(parent1)

    start = random.randint(0, n - 2)
    end = random.randint(start + 1, n - 1)

    child = [-1] * n

    child[start:end] = parent1[start:end]

    pointer = 0

    for value in parent2:

        if value not in child:

            while child[pointer] != -1:
                pointer += 1

            child[pointer] = value

    return child


def mutate(board):

    if random.random() < MUTATION_RATE:

        n = len(board)

        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)

        board[i], board[j] = board[j], board[i]

    return board


def genetic_algorithm(n):

    population = [generate_board(n) for _ in range(POPULATION_SIZE)]

    best_solution = None
    best_conflicts = float("inf")

    for _ in range(GENERATIONS):

        population.sort(key=fitness, reverse=True)

        current_best = population[0]
        current_conflicts = count_conflicts(current_best)

        if current_conflicts < best_conflicts:
            best_conflicts = current_conflicts
            best_solution = current_best[:]

        if current_conflicts == 0:
            return current_best

        selected = selection(population)

        new_population = selected[:ELITE_SIZE]

        while len(new_population) < POPULATION_SIZE:

            parent1 = random.choice(selected)
            parent2 = random.choice(selected)

            child = crossover(parent1, parent2)

            child = mutate(child)

            new_population.append(child)

        population = new_population

    return best_solution


def run_test(n):

    tracemalloc.start()

    start_time = time.time()

    solution = genetic_algorithm(n)

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

        if n > 100:

            print(f"N = {n}")
            print("Skipped: Runtime too high for Genetic Algorithm")

            continue

        run_test(n)