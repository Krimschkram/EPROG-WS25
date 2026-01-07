import numpy as np

def build_A(n):
    A = 4*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    # Liefert matrix mit 4 in der diagonalen und -1 drum herum, k-1 drunter, k = 1 drüber
    return A

def build_C(n):
    A = build_A(n)
    I = np.eye(n)

    C = np.zeros((n*n, n*n))

    for i in range(n): #komplizierter, einfach anschauen nicht so deep
        C[i*n:(i+1)*n, i*n:(i+1)*n] = A

        if i > 0:
            C[i*n:(i+1)*n, (i-1)*n:i*n] = -I
        if i < n-1:
            C[i*n:(i+1)*n, (i+1)*n:(i+2)*n] = -I

    return A, C

# Beispiel
n = 4
A, C = build_C(n)
print("A shape:", A.shape)
print(A)
print("\nC shape:", C.shape)
print(C)
