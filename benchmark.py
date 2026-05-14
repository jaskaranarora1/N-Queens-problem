import csv
import time
import tracemalloc

from exhaustive_dfs import solve_dfs, count_conflicts as dfs_conflicts
from greedy_hill_climbing import min_conflicts, total_conflicts as greedy_conflicts
from simulated_annealing import simulated_annealing, count_conflicts as sa_conflicts
from genetic_algorithm import genetic_algorithm, count_conflicts as ga_conflicts


TEST_CASES = [10, 30, 50, 100, 200, 500]


def measure_algorithm(algorithm_name, function, conflict_function, n):

    tracemalloc.start()

    start_time = time.time()

    try:

        solution = function(n)

        conflicts = conflict_function(solution)

        success = conflicts == 0

    except Exception as e:

        conflicts = f"Error: {e}"
        success = False

    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "Algorithm": algorithm_name,
        "N": n,
        "Success": success,
        "Conflicts": conflicts,
        "Execution Time (s)": round(end_time - start_time, 4),
        "Peak Memory Used (MB)": round(peak / 1024 / 1024, 4)
    }


def main():

    results = []

    for n in TEST_CASES:

        print(f"\n==============================")
        print(f"Running tests for N = {n}")
        print(f"==============================")

        # DFS
        if n == 10:

            print("Running Exhaustive DFS...")

            results.append(
                measure_algorithm(
                    "Exhaustive DFS",
                    solve_dfs,
                    dfs_conflicts,
                    n
                )
            )

        else:

            results.append({
                "Algorithm": "Exhaustive DFS",
                "N": n,
                "Success": "Infeasible",
                "Conflicts": "N/A",
                "Execution Time (s)": "Timeout",
                "Peak Memory Used (MB)": "N/A"
            })

        # Greedy
        if n <= 100:

            print("Running Greedy Hill Climbing...")

            results.append(
                measure_algorithm(
                    "Greedy Hill Climbing",
                    min_conflicts,
                    greedy_conflicts,
                    n
                )
            )

        else:

            results.append({
                "Algorithm": "Greedy Hill Climbing",
                "N": n,
                "Success": "Too Slow",
                "Conflicts": "N/A",
                "Execution Time (s)": "Skipped",
                "Peak Memory Used (MB)": "N/A"
            })

        # Simulated Annealing
        print("Running Simulated Annealing...")

        results.append(
            measure_algorithm(
                "Simulated Annealing",
                simulated_annealing,
                sa_conflicts,
                n
            )
        )

        # Genetic Algorithm
        if n <= 100:

            print("Running Genetic Algorithm...")

            results.append(
                measure_algorithm(
                    "Genetic Algorithm",
                    genetic_algorithm,
                    ga_conflicts,
                    n
                )
            )

        else:

            results.append({
                "Algorithm": "Genetic Algorithm",
                "N": n,
                "Success": "Not Tested",
                "Conflicts": "N/A",
                "Execution Time (s)": "Skipped",
                "Peak Memory Used (MB)": "N/A"
            })

    # Save CSV
    with open("results.csv", "w", newline="") as file:

        fieldnames = [
            "Algorithm",
            "N",
            "Success",
            "Conflicts",
            "Execution Time (s)",
            "Peak Memory Used (MB)"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(results)

    print("\n===================================")
    print("Benchmark completed successfully.")
    print("Results saved to results.csv")
    print("===================================")


if __name__ == "__main__":
    main()