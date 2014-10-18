def is_increasing(seq):
    for i in range(0, len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[j] - seq[i] <= 0:
                return False
    return True
print(is_increasing([1, 2, 30, 10]))
