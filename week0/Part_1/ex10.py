from ex2 import sum_of_digits
def is_number_balanced(n):
	num_of_digits = 0
	k = n
	while k > 0:
		k = k // 10
		num_of_digits += 1
	if num_of_digits % 2 == 0:
		first_half = n // (10 ** (num_of_digits // 2))
		last_half = n % (10 ** (num_of_digits // 2))
	else:
		first_half = n // (10 ** ((num_of_digits // 2) + 1))
		last_half = n % (10 ** (num_of_digits // 2))
	if sum_of_digits(first_half) == sum_of_digits(last_half):
		return True
	else:
		return False

