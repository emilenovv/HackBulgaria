def sum_matrix(m):
    total = 0
    for rows in m:
        for el in rows:
            total += el
    return total

print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))