def count_consonants(str):
	count = 0
	for i in str:
		if i in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
			count += 1
	return count

