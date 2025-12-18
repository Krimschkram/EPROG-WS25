import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
print("Sorted array:", data)

# n = Länge des Arrays
# i \in {0, ..., n-1}
# j \in {0, ..., n-i-2}
# Abschätzung: Σ_{i=0}^{n-1} (n - i - 1)
# mega unnötig



sizes = [100, 200, 400, 800, 1600]
times = []

for n in sizes:
    data = list(range(n, 0, -1))  # worst case, genau falsch rum sortiert
    start = time.time()
    bubble_sort(data)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times, marker='o')
plt.xlabel("n")
plt.ylabel("Zeit (Sekunden)")
plt.title("BubbleSort Laufzeit (worst case)")
plt.show()
