class Matrix:
    """A class to represent a square matrix and perform various operations on it."""

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list[int]:
        if not self.matrix:
            return []
        n = len(self.matrix)
        return [self.matrix[i][i] for i in range(n)]

    def get_counter_diagonal(self) -> list[int]:
        if not self.matrix:
            return []
        n = len(self.matrix)
        return [self.matrix[i][n - 1 - i] for i in range(n)]

    def rotate_rows(self, k: int) -> None:
        if not self.matrix:
            return
        n = len(self.matrix)
        k = k % n
        self.matrix[:] = self.matrix[k:] + self.matrix[:k]

    def rotate_columns(self, k: int) -> None:
        if not self.matrix:
            return
        n = len(self.matrix[0])
        k = k % n
        for row in self.matrix:
            row[:] = row[k:] + row[:k]
