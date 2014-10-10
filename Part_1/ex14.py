def number_to_list(n):
    lst = []
    for i in str(n):
        lst.append(i)
    map(int(), lst)
    return lst

print(number_to_list(15645))