import numpy as np
import matplotlib.pyplot as plt


data = np.load("xy1d.npy")
print("Geladen:", type(data), "shape:", data.shape, "ndim:", data.ndim)


# 3) In eine nützliche Form bringen: (N, 2) mit reshape
xy = data.reshape(-1, 2)   # jede Zeile: [x, y], -1 bestimmt Zeilen Automatisch
x = xy[:, 0] # slicing Dopelunkt heißt "alle" , 0 heißt spalte
y = xy[:, 1]


# 4) Plot: x gegen y
plt.figure()
plt.plot(x, y)             # alternativ: plt.scatter(x, y, s=5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot aus xy1d.npy")

# 5) Achsen gleich skalieren
plt.axis("equal")
plt.grid(True)
plt.show()
