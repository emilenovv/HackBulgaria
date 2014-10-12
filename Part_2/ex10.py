def magic_square(matrix):
    example_sum = 0
    total = 0
    for row in matrix:
        print(row)  # prints the square
    for el in matrix[0]:
        example_sum += el
    for row in matrix:
        total = 0
        for el in row:
            total += el
        if total != example_sum:  # checks if the sum of the elements in rows equals the example_sum
            return False
    total = 0
    for i in range(len(matrix)):
        total = 0
        for j in range(len(matrix)):
            total += matrix[j][i]
        if total != example_sum:  # # checks if the sum of the elements in colons equals the example_sum
            return False
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    if total != example_sum:  # checks the sum of the el. of the main diag.
        return False
    total = 0
    for i in range(len(matrix)):
        total += matrix[len(matrix) - i - 1][i]
    if total != example_sum:
        return False
    return True
