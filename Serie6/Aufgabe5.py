def determinant(matrix):
    # Basisfall für 1x1
    if len(matrix) == 1:
        return matrix[0][0]

    # Basisfall für 2x2
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0

    # Entwicklung entlang der ersten Zeile
    for col in range(len(matrix)):
        # Minor bilden: ohne Zeile 0 und ohne Spalte col
        minor = [
            [matrix[i][j] for j in range(len(matrix)) if j != col]
            for i in range(1, len(matrix))
        ]
        print(minor)

        # Vorzeichen: + - + - + ...
        sign = (-1) ** col

        det += sign * matrix[0][col] * determinant(minor)

    return det
A = [
    [2, 1, 3, 4],
    [0, 1, -1, 2],
    [5, 2, 0, -3],
    [1, 4, 2, 1]
]

print(determinant(A))
