def sort_fractions(fractions):
    nominator = 0
    denominator = 0
    results = {}
    result = 0
    for fraction in fractions:
        nominator = fraction[0]
        denominator = fraction[1]
        result = nominator / denominator
        results[(nominator, denominator)] = result
    results = sorted(results, key=results.get)
    return results