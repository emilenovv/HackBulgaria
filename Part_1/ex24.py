def iterations_of_nan_expand(n):
    if n == "":
        return 0
    else:
        k = n
        if "Not a " in k:
            k = k.replace("Not a ", "")
        if k != "NaN":
            return False
        else:
            return n.count("Not a ")
