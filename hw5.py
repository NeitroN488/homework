from fractions import Fraction

class FractionMatrix:
    def __init__(self, matrix_data):
        self.matrix = []
        for row in matrix_data:
            self.matrix.append([Fraction(x) for x in row]) 
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0]) if self.rows > 0 else 0
        if any(len(row) != self.cols for row in self.matrix):
            raise ValueError("")

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(str(x) for x in row) + "\n"
        return matrix_str

    def __add__(self, other):
        if not isinstance(other, FractionMatrix):
            raise TypeError("")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return FractionMatrix(result)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def transpose(self):
        pass

    def determinant(self):
        pass

    @staticmethod
    def is_valid_matrix_data(matrix_data):
        pass

    @classmethod
    def identity_matrix(cls, n):
        pass

    @property
    def shape(self):
        return (self.rows, self.cols)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

# Пример использования:
m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(2, 5), Fraction(2, 5)]])

print("Матрица m1:")
print(m1)

print("Матрица m2:")
print(m2)

print("Сложение m1 + m2:")
print(m1 + m2)
