from ex8 import contains_digit
def contains_digits(number, digits):
	for i in digits:
		if not contains_digit(number, i):
			return False
	return True

print(contains_digits(456, []))