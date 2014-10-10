def sevens_in_a_row(arr, n):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == 7:
            count = 0
            if i + n < len(arr):
                for j in range(i, i + n):
                    if arr[j] == 7:
                        count += 1
                if count == n:
                    return True
    return False

print(sevens_in_a_row([7, 2, 1, 6, 2], 1))
