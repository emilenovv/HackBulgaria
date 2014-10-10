from ex7 import is_int_palindrome


def is_hack(n):
    count_ones = 0
    bin_num = "{0:b}".format(n)
    bin_num = int(bin_num)
    k = bin_num
    while k > 0:
        if k % 10 == 1:
            count_ones += 1
        k //= 10
    if is_int_palindrome(bin_num) and count_ones % 2 != 0:
        return True
    else:
        return False


def next_hack(n):
    n += 1
    while not is_hack(n):
        n += 1
    return n
print(next_hack(0))
