import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]      # Pivot = mittleres Element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def worst_case_same_elements(n):
    # Alle Elemente sind gleich
    # left = [], right = []
    # In jedem Rekursionsschritt werden wieder n Elemente betrachtet
    return [1] * n


def worst_case_unbalanced(n):
    # Konstruktion eines Arrays, das zu sehr unausgeglichenen Partitionen führt
    arr = list(range(1, n))
    arr.insert(len(arr)//2, 0)  # kleinstes Element in die Mitte
    return arr

def measure_time(data):
    start = time.time()
    quicksort(data)
    end = time.time()
    return end - start


sizes = [100, 200, 400, 800, 1600]

times_same = []
times_unbalanced = []

for n in sizes:
    data1 = worst_case_same_elements(n)
    data2 = worst_case_unbalanced(n)

    times_same.append(measure_time(data1))
    times_unbalanced.append(measure_time(data2))

plt.plot(sizes, times_same, marker='o', label="Alle Elemente gleich")
plt.plot(sizes, times_unbalanced, marker='o', label="Unausgeglichene Teilung")

plt.xlabel("n")
plt.ylabel("Zeit (Sekunden)")
plt.title("QuickSort Worst-Case-Laufzeit")
plt.legend()
plt.show()
