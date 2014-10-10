def prepare_meal(number):
    EGGS = 'eggs'
    AND = 'and '
    SPAM = 'spam '
    result = ''
    while number % 3 == 0:
        result += SPAM
        number /= 3
    while number % 5 == 0:
        if result == '':
            result += EGGS
        else:
            result += AND
            result += EGGS
        number /= 5
    return result

print(prepare_meal(15))
        



