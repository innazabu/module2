def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        a=[]
        for j in range(m):
            a.append(value)
        matrix.append(a)
    return matrix

print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
