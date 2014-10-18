def zero_insert(n):
    n = str(n)
    pos = 0
    for i in range(0, len(n) - 1):
        print(i)
        if n[i] == n[i + 1] or (int(n[i]) + int(n[i + 1])) % 10 == 0:
            pos += 1
    for i in range(0, len(n) + pos - 1):
        if n[i] == n[i + 1] or (int(n[i]) + int(n[i + 1])) % 10 == 0:
            n = n[:i + 1] + '0' + n[i + 1:]
    return int(n)

print(zero_insert(1))
