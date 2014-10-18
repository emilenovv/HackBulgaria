def nth_fib_lists(listA, listB, n):
    first_list = listA
    second_list = listB
    if n == 1:
        return first_list
    elif n == 2:
        return second_list
    else:
        return nth_fib_lists(listA, listB, n - 2) + nth_fib_lists(listA, listB, n - 1)
