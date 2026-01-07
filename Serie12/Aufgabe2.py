import numpy as np
import time
import matplotlib.pyplot as plt

ns = [50, 100, 200, 400, 800, 1600, 3200, 6400]
times = []

for n in ns:
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    t0 = time.time()
    A @ B
    t1 = time.time()

    times.append(t1 - t0)

plt.loglog(ns, times, marker="o")
plt.xlabel("n")
plt.ylabel("Zeit")
plt.title("Matrix-Matrix-Multiplikation")
plt.show()

# m = 50, n = 100, extrem schnell
# dann einbruch, und dann Linear, nicht vergessen, loglog