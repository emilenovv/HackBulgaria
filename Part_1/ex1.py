def nth_fibonacci(n):
	fib1 = 1
	fib2 = 1
	for i in range(2, n):
		fib = fib1
		fib1 = fib1 + fib2
		fib2 = fib
	return fib1

print(nth_fibonacci(10))