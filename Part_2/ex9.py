def nth_fib_lists(listA, listB, n):
    first_list = listA
    second_list = listB
    for i in range(1, n):
        temp = first_list
        first_list = first_list + second_list
        second_list = temp
    return first_list
