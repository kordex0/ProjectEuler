def problem002():
    a = 1
    b = 1
    total = 0
    while b < 4000000:
        if b % 2 == 0:
            total += b
        tmp = a + b
        a = b
        b = tmp
    return total

print(problem002())
