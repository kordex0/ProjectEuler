

def problem067():
    s = open('problem067_triangle.txt', 'r')
    a = []
    for line in reversed(list(s)):
        numbers = line.split(" ")
        if len(a) == 0:
            a = [0]*(len(numbers)+1)
        for i in range(len(numbers)):
            a[i] = max(a[i], a[i+1]) + int(numbers[i])
    return a[0]

print(problem067())
