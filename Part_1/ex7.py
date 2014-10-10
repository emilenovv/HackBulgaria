def is_int_palindrome(n):
	back = ""
	back = str(n)
	back = back[::-1]
	back = int(back)
	if n == back:
		return True
	else:
		return False
