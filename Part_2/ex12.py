def subsquare(matrix, x, y):
    result = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            result.append(matrix[i][j])
    return result


def digit_only_once(lst):
    count_digits = {}
    for i in range(1, 10):
        count_digits[i] = 0
    for digit in lst:
        count_digits[digit] += 1
    for key in count_digits:
        if count_digits[key] != 1:
            return False
    return True




def sudoku_solved(sudoku):
    count_num = {}
    for i in range(1, 10):
        count_num[i] = 0
    for row in sudoku:
        for el in row:
            count_num[el] += 1
    for key in count_num:
        if count_num[key] != 9:
            return False
    for i in range(1, 10):
        count_num[i] = 0
    for i in range(9):
        for j in range(9):
            count_num[sudoku[j][i]] += 1
    for key in count_num:
        if count_num[key] != 9:
            return False
    i = 0
    j = 0
    while i < 9:
        j = 0
        while j < 9:
            print(subsquare(sudoku, i, j))
            if not digit_only_once(subsquare(sudoku, i, j)):
                return False
            j += 3 
        i += 3
    return True
