def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        a=[]
        for j in range(m):
            a.append(value)
        matrix.append(a)
    return matrix

print(get_matrix(7, 2, 13))
