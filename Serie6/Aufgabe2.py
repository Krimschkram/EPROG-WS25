def LxV(L, vector):
    n = len(L)
    new_vect = [0] * n        
    for i in range(n):
        for j in range(i + 1): # nur bis i laufen (j = 0..i), da L[i][j] = 0 für j > i
            new_vect[i] += L[i][j] * vector[j]

    return new_vect

L_test = [
    [4, 0, 0],
    [2, 5, 0],
    [1, 3, 6]
]

# Vektor v
v_test = [10, 2, 5]

# Berechnung: y = L * v
result_y = LxV(L_test, v_test)
print(result_y)