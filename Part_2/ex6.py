def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    nominator_divisors = find_divisors(nominator)
    denominator_divisors = find_divisors(denominator)
    mutual_divisors = []
    for num in nominator_divisors:
        if num in denominator_divisors:
            mutual_divisors.append(num)
    mutual_divisors.remove(1)
    for div in mutual_divisors:
        while nominator % div == 0 and denominator % div == 0:
            nominator /= div
            denominator /= div
    return tuple([int(nominator), int(denominator)])