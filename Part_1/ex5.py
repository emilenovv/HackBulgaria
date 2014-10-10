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

def prime_number_if_divisors(n):
	count = 0
	for i in range(1, n + 1):
		if n % i == 0:
			count += 1
	return is_prime(count)

print(prime_number_if_divisors(9))