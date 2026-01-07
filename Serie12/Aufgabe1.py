import numpy as np

A = np.array([[1, 1, 2],
              [2, 3, 1],
              [7, 9, -3]])

Y = np.array([3, 5, 0])

X = np.linalg.solve(A, Y)
print(X)

A_inv = np.linalg.inv(A)
X_new = A_inv.dot(Y)
print(X_new)
print()

print(A.dot(X))
print(A.dot(X_new))