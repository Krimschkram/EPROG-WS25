import numpy as np


def viertel(A):
    n = len(A)
    m = n // 2
    return A[:m, :m], A[:m, m:], A[m:, :m], A[m:, m:]


def zusammenbauen(C11, C12, C21, C22):
    return np.vstack((np.hstack((C11, C12)),
                      np.hstack((C21, C22))))
# hstack...horizontales Stapeln von Arrays
# vstack...vertikales Stapeln von Arrays


def matrix_rekurs_multipl(A, B):
    n = A.shape[0]
    if n <= 2:
        return A @ B

    A11, A12, A21, A22 = viertel(A)
    B11, B12, B21, B22 = viertel(B)

    M1 = matrix_rekurs_multipl(A11 + A22, B11 + B22)
    M2 = matrix_rekurs_multipl(A21 + A22, B11)
    M3 = matrix_rekurs_multipl(A11, B12 - B22)
    M4 = matrix_rekurs_multipl(A22, B21 - B11)
    M5 = matrix_rekurs_multipl(A11 + A12, B22)
    M6 = matrix_rekurs_multipl(A21 - A11, B11 + B12)
    M7 = matrix_rekurs_multipl(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    return zusammenbauen(C11, C12, C21, C22)


# Was für Aufwand zeigen, wie schau ich aus
