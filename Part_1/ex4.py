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
