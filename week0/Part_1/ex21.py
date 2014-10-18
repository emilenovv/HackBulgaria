def print_matrix(m):
    for rows in m:
        row_str = ""
        for el in rows:
            row_str += " {} ".format(el)
        print(row_str)

def matrix_bombing_plan(m):
    