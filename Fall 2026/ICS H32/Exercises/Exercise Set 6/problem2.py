def reverse_transpose(matrix: list[list[object]]) -> list[list[object]]:
    row_count = len(matrix)
    column_count = len(matrix[0])
    return [[matrix[row_count - 1 - j][column_count - 1 - i]
             for j in range(row_count)]
            for i in range(column_count)]


def calculate_sums(numbers: list[list[float]]) -> None:
    for i in range(len(numbers) - 1, -1, -1):
        for j in range(len(numbers[i]) - 1, -1, -1):
            total = numbers[i][j]

            if i + 1 < len(numbers):
                total += numbers[i + 1][j]

            if j + 1 < len(numbers[i]):
                total += numbers[i][j + 1]

            # The cell below-right was added twice, so take it back out.
            if i + 1 < len(numbers) and j + 1 < len(numbers[i]):
                total -= numbers[i + 1][j + 1]

            numbers[i][j] = total
