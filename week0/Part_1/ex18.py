def decreasing(seq):
    for i in range(0, len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[j] - seq[i] >= 0:
                return False
    return True
