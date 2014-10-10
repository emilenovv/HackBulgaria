def biggest_difference(arr):
    big_diff = arr[1] - arr[0]
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > big_diff:
                big_diff = arr[j] - arr[i]
    return big_diff