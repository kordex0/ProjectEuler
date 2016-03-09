def problem001():
    total = 0
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(problem1())
