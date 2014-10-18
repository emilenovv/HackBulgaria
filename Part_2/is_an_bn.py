def is_an_bn(word):
    count_a = 0
    count_b = 0
    length = len(word)
    half_length = length // 2
    if length % 2 != 0:
        return False
    else:
        first_half = word[:half_length]
        second_half = word[half_length:]
        for char in first_half:
            if char == 'a':
                count_a += 1
        for char in second_half:
            if char == 'b':
                count_b += 1
        if count_a == count_b:
            return True
        else:
            return False
