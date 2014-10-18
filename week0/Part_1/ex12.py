def count_vowels(str):
	count = 0
	for i in str:
		if i in "aeiouyAEIOUY":
			count += 1
	return count

