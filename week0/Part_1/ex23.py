def nan_expand(n):
    not_a = "Not a "
    NaN = "Not a NaN"
    if n == 0:
        return ""
    else:
        return (n - 1) * not_a + NaN

print(nan_expand(1))
