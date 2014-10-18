def sum_of_devisors(n):
	total = 0
	for i in range(1, n + 1):
		if n % i == 0:
			total += i
	return total

print(sum_of_devisors(8))