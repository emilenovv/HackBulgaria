def is_prime(n):
    b = 1
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                b = 0
        if b == 0:
            return False
        else:
            return True


def prime_range(n):
    result = []
    for i in range(n + 1):
        if is_prime(i):
            result.append(i)
    return result


def goldbach_conjecture(n):
    result = []
    if n % 2 == 0:
        if n > 2:
            for i in prime_range(n):
                for j in prime_range(n):
                    if i + j == n and i <= j:
                        result.append((i, j))
    return result 