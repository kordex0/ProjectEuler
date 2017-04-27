
from timeit import timeit

def mat_mul(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] = c[i][j] + a[i][k]*b[k][j]
    return c

def mat_mul_2(a, b):
    return [[a[0][0]*b[0][0]+a[0][1]*b[1][0],
             a[0][0]*b[0][1]+a[0][1]*b[1][1]],
            [a[1][0]*b[0][0]+a[1][1]*b[1][0],
             a[1][0]*b[0][1]+a[1][1]*b[1][1]]]

def mat_pow(m, p):
    if p % 2 == 1:
        if p == 1:
            return m
        return mat_mul_2(m, mat_pow(m, p-1))
    else:
        mp = mat_pow(m, p//2)
        return mat_mul_2(mp, mp)

def mat_fib(n):
    if n == 1:
        return 1
    return sum(mat_pow([[0, 1], [1, 1]], n-1)[1])

def mat_fib2(n):
    if n == 1:
        return 1
    if (n-1) % 2 == 1:
        mp = mat_pow([[0, 1], [1, 1]], n-2)
        return mp[0][0] + mp[0][1] + mp[1][0] + mp[1][1]
    else:
        mp = mat_pow([[0, 1], [1, 1]], (n-1)//2)
        return mp[0][0]*mp[1][0]+mp[1][0]*mp[1][1]+mp[0][1]*mp[1][0]+mp[1][1]*mp[1][1]

def fib(n):
    a = 0
    b = 1
    for i in range(n):
        tmp = b
        b += a
        a = tmp
    return b


