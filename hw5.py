#     def transpose(self):
#         result = [[self._matrix[j][i] for j in range(self._rows)] for i in range(self._cols)]
#         return FractionMatrix(result)

#     @property
#     def determinant(self):
#         if self._rows != self._cols:
#             raise ValueError("Определитель можно вычислить только для квадратных матриц.")

#         if self._rows == 1:
#             return self._matrix[0][0]
#         elif self._rows == 2:
#             return self._matrix[0][0] * self._matrix[1][1] - self._matrix[0][1] * self._matrix[1][0]
#         else:
#             det = Fraction(0, 1)
#             for j in range(self._cols):
#                 submatrix = [row[:j] + row[j+1:] for row in self._matrix[1:]]
#                 sign = Fraction(1, 1) if j % 2 == 0 else Fraction(-1, 1)
#                 det += sign * self._matrix[0][j] * FractionMatrix(submatrix).determinant
#             return det

#     @staticmethod
#     def check_dimensions(matrix1, matrix2, operation):
#         if operation == "addition" or operation == "subtraction":
#             if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
#                 raise ValueError("Матрицы должны иметь одинаковые размеры для сложения/вычитания.")
#         elif operation == "multiplication":
#             if matrix1.cols != matrix2.rows:
#                 raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")
#         elif operation == "determinant":
#             if matrix1.rows != matrix1.cols:
#                 raise ValueError("Определитель можно вычислить только для квадратных матриц.")
#         else:
#             raise ValueError("Неизвестная операция.")
    
#     @classmethod
#     def create_identity_matrix(cls, size):
#         identity_matrix = [[Fraction(1, 1) if i == j else Fraction(0, 1) for j in range(size)] for i in range(size)]
#         return cls(identity_matrix)

#     def new(cls, matrix):
#         if not isinstance(matrix, list):
#             raise TypeError("Матрица должна быть представлена в виде списка списков.")
#         if not all(isinstance(row, list) for row in matrix):
#             raise TypeError("Каждая строка матрицы должна быть списком.")
#         if not all(isinstance(x, (int, Fraction)) for row in matrix for x in row):
#             raise TypeError("Все элементы матрицы должны быть целыми числами или дробями.")
#         if len(matrix) > 0:
#             row_len = len(matrix[0])
#             if not all(len(row) == row_len for row in matrix):
#                 raise ValueError("Все строки матрицы должны иметь одинаковую длину.")

#         instance = super().new(cls)
#         return instance    
# m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
# m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
# print("m1:")
# print(m1)
# print("\nm2:")
# print(m2)

# print("\nm1 + m2:")
# print(m1 + m2)
# print("\nm1 * m2:")
# print(m1 * m2) 
# print("\nОпределитель m1:")
# print(m1.determinant) 
# print("\nТранспонированная m1:")
# print(m1.transpose())
