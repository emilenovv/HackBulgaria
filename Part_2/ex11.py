def groupby(func, seq):
    result = {}
    print(fuct(5), func(10))
    for item in seq:
        result.setdefault(func(item), []).append(item)
    return result

