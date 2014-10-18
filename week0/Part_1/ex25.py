from ex4 import is_prime


def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def prime_factorization(n):
    result = []
    power = 0
    prime_divisors = []
    for i in find_divisors(n):
        if is_prime(i):
            prime_divisors.append(i)
    for i in prime_divisors:
        power = 0
        while n % i == 0:
            n /= i
            power += 1
        result.append(tuple([i, power]))
    return result



    
print(prime_factorization(1565456))
