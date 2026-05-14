# Solving the N-Queens Problem with Exhaustive Search, Local Search, Simulated Annealing and Genetic Algorithm

## Project Overview

This project solves the N-Queens problem using four different algorithmic approaches:

1. Exhaustive Depth-First Search
2. Greedy Hill Climbing / Min-Conflicts
3. Simulated Annealing
4. Genetic Algorithm

The performance of each algorithm is compared for:

- N = 10
- N = 30
- N = 50
- N = 100
- N = 200
- N = 500

The comparison is based on:

- Correctness
- Number of conflicts
- Execution time
- Memory usage

---

## Problem Description

The N-Queens problem requires placing N queens on an N × N chessboard so that no two queens attack each other.

Queens attack each other if they share:

- Same row
- Same column
- Same diagonal

In this implementation, the board is represented as a one-dimensional list.

Example:

```python
[0, 2, 5, 7, 9, 4, 8, 1, 3, 6]