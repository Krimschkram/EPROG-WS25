def matrix_summen(matrix_3x3):
    x = matrix_3x3[0][0] + matrix_3x3[0][1] + matrix_3x3[0][2]
    y = matrix_3x3[1][0] + matrix_3x3[1][1] + matrix_3x3[1][2]
    z = matrix_3x3[2][0] + matrix_3x3[2][1] + matrix_3x3[2][2]

    print("Zeilensummennorm:",x, y, z)

    x = matrix_3x3[0][0] + matrix_3x3[1][0] + matrix_3x3[2][0]
    y = matrix_3x3[0][0] + matrix_3x3[1][1] + matrix_3x3[2][2]
    z = matrix_3x3[2][0] + matrix_3x3[2][1] + matrix_3x3[2][2]

    print("Spaltensummennorm:",x, y, z)

    x = matrix_3x3[0][0] + matrix_3x3[1][1] + matrix_3x3[2][2]
    print("Diagonalsumme:", x)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_summen(matrix)