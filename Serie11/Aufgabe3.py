import time
import sys
import matplotlib.pyplot as plt



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]      # Pivot = mittleres Element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# OPTIMAL / "GUT": balancierte Teilungen => O(n log n)
def best_case_balanced(n):
    return list(range(n))  # sortiert, Pivot ist ungefähr Median


# SUBOPTIMAL / WORST: in jedem Schritt extrem unbalanciert => O(n^2)
def worst_case_mid_pivot(n):
    L = []
    for x in range(n - 1, -1, -1):
        L.insert(len(L) // 2, x)
    print(L)
    return L


def measure_time(data, repeats=3):
    best = float("inf")
    for _ in range(repeats):
        start = time.time()
        quicksort(data)
        end = time.time()
        best = min(best, end - start)
    return best


sizes = [100, 200, 400, 800, 1200, 1600]

times_best = []
times_worst = []

for n in sizes:
    data_best = best_case_balanced(n)
    data_worst = worst_case_mid_pivot(n)

    times_best.append(measure_time(data_best))
    times_worst.append(measure_time(data_worst))

plt.plot(sizes, times_best, marker='o', label="Optimal (balanciert) ~ O(n log n)")
plt.plot(sizes, times_worst, marker='o', label="Suboptimal (Worst-Case) ~ O(n^2)")

plt.xlabel("n")
plt.ylabel("Zeit (Sekunden)")
plt.title("QuickSort: optimal vs. suboptimal (Pivot = mittleres Element)")
plt.legend()
plt.show()
