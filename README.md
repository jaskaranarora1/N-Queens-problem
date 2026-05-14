# ♟️ Solving the N-Queens Problem using Exhaustive Search, Local Search and Optimization Algorithms

## 📌 Project Overview

This project solves the classical **N-Queens Problem** using four different Artificial Intelligence and Optimization approaches:

1. Exhaustive Depth-First Search (DFS)
2. Greedy Hill Climbing / Min-Conflicts
3. Simulated Annealing
4. Genetic Algorithm

The algorithms are implemented in Python and compared based on:

* Correctness
* Number of conflicts
* Execution time
* Peak memory usage
* Scalability

The implementations are tested for the following board sizes:

```text
N = 10, 30, 50, 100, 200, 500
```

---

# 📖 What is the N-Queens Problem?

The N-Queens problem is a classical constraint satisfaction and optimization problem.

The objective is:

> Place N queens on an N × N chessboard such that no two queens attack each other.

A queen attacks another queen if they are placed:

* In the same row
* In the same column
* In the same diagonal

---

# 🧠 Example Representation

The board is represented using a one-dimensional list.

Example:

```python
[0, 2, 5, 7, 9, 4, 8, 1, 3, 6]
```

This means:

```text
Row 0 → Column 0
Row 1 → Column 2
Row 2 → Column 5
...
```

Each index represents the row and each value represents the column.

---

# 🚀 Algorithms Implemented

---

## 1️⃣ Exhaustive Depth-First Search (DFS)

### Description

DFS uses recursive backtracking to place queens row-by-row.

If a queen placement becomes invalid, the algorithm backtracks and tries another position.

### Advantages

* Guarantees a correct solution
* Simple and deterministic

### Disadvantages

* Extremely slow for large N
* Exponential complexity

### Complexity

```text
Time Complexity: O(N!)
```

### Usage in this project

Tested only for:

```text
N = 10
```

because larger board sizes become computationally infeasible.

---

## 2️⃣ Greedy Hill Climbing / Min-Conflicts

### Description

Starts from a random board and repeatedly moves conflicted queens to reduce the number of conflicts.

### Advantages

* Faster than exhaustive search
* Uses local optimization

### Disadvantages

* Can get stuck in local minima
* Runtime increases significantly for large N

### Usage in this project

Tested up to:

```text
N = 100
```

Skipped for:

```text
N = 200, 500
```

because runtime becomes too high.

---

## 3️⃣ Simulated Annealing

### Description

Simulated Annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy.

It sometimes accepts worse states to escape local minima.

### Advantages

* Escapes local optima
* Better scalability than greedy search
* Works for large N

### Disadvantages

* May return near-optimal solutions
* Performance depends on temperature and cooling rate

---

## 4️⃣ Genetic Algorithm

### Description

The Genetic Algorithm evolves a population of candidate solutions using:

* Selection
* Crossover
* Mutation
* Elitism

### Advantages

* Strong optimization capability
* Good scalability
* Produces high-quality solutions

### Disadvantages

* Slower than local search
* Requires parameter tuning

### Features used in this implementation

* Permutation-based board representation
* Order crossover
* Swap mutation
* Elitism

### Usage in this project

Tested up to:

```text
N = 100
```

Skipped for:

```text
N = 200, 500
```

because runtime becomes too high.

---

# 📂 Project Structure

```text
nqueens_project/
│
├── exhaustive_dfs.py
├── greedy_hill_climbing.py
├── simulated_annealing.py
├── genetic_algorithm.py
├── benchmark.py
├── generate_graphs.py
├── board_visualization.py
├── results.csv
└── README.md
```

---

# ⚙️ Requirements

## Software Requirements

* Python 3.9 or higher
* pip

## Required Python Libraries

```bash
pip install pandas matplotlib psutil
```

---

# 🖥️ Installation Guide

---

# 🍎 Setup on macOS

## Step 1 — Open Terminal

Create project directory:

```bash
mkdir nqueens_project
cd nqueens_project
```

## Step 2 — Create Virtual Environment

```bash
python3 -m venv .venv
```

## Step 3 — Activate Virtual Environment

```bash
source .venv/bin/activate
```

You should see:

```bash
(.venv)
```

## Step 4 — Install Dependencies

```bash
pip install pandas matplotlib psutil
```

## Step 5 — Run Individual Algorithms

### DFS

```bash
python3 exhaustive_dfs.py
```

### Greedy Hill Climbing

```bash
python3 greedy_hill_climbing.py
```

### Simulated Annealing

```bash
python3 simulated_annealing.py
```

### Genetic Algorithm

```bash
python3 genetic_algorithm.py
```

## Step 6 — Run Benchmark

```bash
python3 benchmark.py
```

This generates:

```text
results.csv
```

## Step 7 — Generate Comparison Graphs

```bash
python3 generate_graphs.py
```

Generated files:

```text
runtime_comparison.png
memory_comparison.png
conflicts_comparison.png
```

## Step 8 — Generate Board Visualization

```bash
python3 board_visualization.py
```

Generated file:

```text
board_visualization.png
```

---

# 🪟 Setup on Windows

## Step 1 — Open CMD or PowerShell

Create project folder:

```bash
mkdir nqueens_project
cd nqueens_project
```

## Step 2 — Create Virtual Environment

```bash
python -m venv .venv
```

## Step 3 — Activate Virtual Environment

### CMD

```bash
.venv\Scripts\activate
```

### PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks execution:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again.

## Step 4 — Install Dependencies

```bash
pip install pandas matplotlib psutil
```

## Step 5 — Run Algorithms

```bash
python exhaustive_dfs.py
python greedy_hill_climbing.py
python simulated_annealing.py
python genetic_algorithm.py
```

## Step 6 — Run Benchmark

```bash
python benchmark.py
```

This creates:

```text
results.csv
```

## Step 7 — Generate Graphs

```bash
python generate_graphs.py
```

## Step 8 — Generate Board Visualization

```bash
python board_visualization.py
```

---

# ▶️ Running the Complete Project

After installing dependencies, run:

## macOS

```bash
python3 benchmark.py
python3 generate_graphs.py
python3 board_visualization.py
```

## Windows

```bash
python benchmark.py
python generate_graphs.py
python board_visualization.py
```

---

# 📊 Benchmarking

The benchmark compares:

* Execution Time
* Peak Memory Usage
* Number of Conflicts
* Success Rate

The benchmark output is stored in:

```text
results.csv
```

---

# 📈 Generated Graphs

## Runtime Comparison

```text
runtime_comparison.png
```

Compares execution time for all algorithms.

---

## Memory Comparison

```text
memory_comparison.png
```

Compares peak memory usage.

---

## Conflict Comparison

```text
conflicts_comparison.png
```

Compares number of conflicts in final solutions.

---

# ♟️ Board Visualization

```text
board_visualization.png
```

Contains:

1. Empty Chessboard
2. Incorrect Queen Placement
3. Correct Queen Placement

Used for visual explanation in the report.

---

# 📋 Example Benchmark Results

| Algorithm           | N   | Conflicts     | Time      |
| ------------------- | --- | ------------- | --------- |
| DFS                 | 10  | 0             | Very Fast |
| Greedy              | 100 | Few conflicts | Slow      |
| Simulated Annealing | 500 | Approximate   | Moderate  |
| Genetic Algorithm   | 100 | 0             | Good      |

---

# 🔬 Observations

## DFS

* Exact but not scalable

## Greedy Hill Climbing

* Suffers from local minima
* Runtime increases heavily

## Simulated Annealing

* Better exploration
* Works for larger N

## Genetic Algorithm

* Best overall scalability
* Produces high-quality solutions

---

# 📚 Technologies Used

* Python
* Pandas
* Matplotlib
* Tracemalloc
* CSV

---

# 📌 Notes

* DFS becomes infeasible for large N because of exponential complexity.
* Greedy Hill Climbing and Genetic Algorithm are skipped for some large N values due to very high runtime.
* Simulated Annealing and Genetic Algorithm are stochastic algorithms, so results may vary between executions.

---

# 👨‍💻 Author

## Vikash

Project:

```text
Solving the N-Queens Problem using Exhaustive Search,
Local Search and Optimization Algorithms
```

---

# 📜 License

This project is developed for educational and academic purposes.
