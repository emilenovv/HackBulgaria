def contains_digit(number, digit):
	while number > 0:
		k = number % 10
		number = number // 10
		if k == digit:
			return True
	return False
