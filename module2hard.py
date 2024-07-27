import random


def first():
    c = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    r = random.choice(c)
    return r


n = first()
result = ''
for i in range(1, n):
    for j in range(i, n):
        if n % (i + j) == 0 and i != j:
            result += str(i) + str(j)

print(n, result)