class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(self.matrix)    #zeilen
        self.m = len(self.matrix[0]) #spalten

    def __str__(self):
        ret = ""
        for row in self.matrix:
            ret += str(row) + "\n"
        return ret

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Matrix muss gleiche Größe haben, trottl")
        ret = [[0]*self.m for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                ret[i][j] = other.matrix[i][j] + self.matrix[i][j]
        return Matrix(ret)

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Anzahl der Spalten von self muss der Anzahl der Zeilen von other entsprechen.")

        result = [[0] * other.m for _ in range(self.n)]

        for i in range(self.n):  # Zeile in A
            for j in range(other.m):  # Spalte in B
                for k in range(self.m):  # Laufindex
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(result)



matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(matrix + matrix2)

print()
matrix = Matrix([[1,2,3]])
matrix2 = Matrix([[4], [5], [6]])

print(matrix * matrix2)

matrix = Matrix([[1,2,3], [4,5,6]])
matrix2 = Matrix([[1, 2], [3, 4], [5,6]])

print(matrix * matrix2)