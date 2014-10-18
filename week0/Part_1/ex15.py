def list_to_number(digits):
	num = 0
	num_of_digits = len(digits)
	for i in digits:
		print(i)
		num += (10 ** num_of_digits) * digits[i]
		#print(num)
		num_of_digits -= 1
	return num

print(list_to_number([2, 3, 6, 8]))
