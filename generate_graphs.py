import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("results.csv")

# Convert numeric columns safely
df["Execution Time (s)"] = pd.to_numeric(df["Execution Time (s)"], errors="coerce")
df["Peak Memory Used (MB)"] = pd.to_numeric(df["Peak Memory Used (MB)"], errors="coerce")
df["Conflicts"] = pd.to_numeric(df["Conflicts"], errors="coerce")


# 1. Runtime comparison
plt.figure(figsize=(10, 6))

for algorithm in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algorithm]
    plt.plot(subset["N"], subset["Execution Time (s)"], marker="o", label=algorithm)

plt.xlabel("Number of Queens (N)")
plt.ylabel("Execution Time (seconds)")
plt.title("Runtime Comparison of N-Queens Algorithms")
plt.legend()
plt.grid(True)
plt.savefig("runtime_comparison.png", dpi=300, bbox_inches="tight")
plt.close()


# 2. Memory comparison
plt.figure(figsize=(10, 6))

for algorithm in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algorithm]
    plt.plot(subset["N"], subset["Peak Memory Used (MB)"], marker="o", label=algorithm)

plt.xlabel("Number of Queens (N)")
plt.ylabel("Peak Memory Used (MB)")
plt.title("Memory Usage Comparison of N-Queens Algorithms")
plt.legend()
plt.grid(True)
plt.savefig("memory_comparison.png", dpi=300, bbox_inches="tight")
plt.close()


# 3. Conflict comparison
plt.figure(figsize=(10, 6))

for algorithm in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == algorithm]
    plt.plot(subset["N"], subset["Conflicts"], marker="o", label=algorithm)

plt.xlabel("Number of Queens (N)")
plt.ylabel("Number of Conflicts")
plt.title("Conflict Comparison of N-Queens Algorithms")
plt.legend()
plt.grid(True)
plt.savefig("conflicts_comparison.png", dpi=300, bbox_inches="tight")
plt.close()


print("Graphs generated successfully:")
print("runtime_comparison.png")
print("memory_comparison.png")
print("conflicts_comparison.png")