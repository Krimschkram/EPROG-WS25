def reverse_rows_references(matrix):
    return matrix[::-1]   # nur Referenzen werden umgedreht

def reverse_rows_copy(matrix):
    return [row[:] for row in matrix[::-1]]  # tiefe Kopie der Zeilen

A = [
    [1, 2],
    [3, 4]
]

# Variante A (Referenzen)
R1 = reverse_rows_references(A)

R1[0][0] = 999    # wir ändern R1

print("A nach Änderung in R1:", A)


A = [
    [1, 2],
    [3, 4]
]

R2 = reverse_rows_copy(A)
R2[0][0] = 999

print("A nach Änderung in R2:", A)  # A bleibt unverändert -> unabhängig!