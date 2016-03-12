
def problem047():
    factors = [0]*1000000
    count = 0
    for i in range(2, 1000000):
        if factors[i] == 0:
            count = 0
            tmp = i
            while tmp < 1000000:
                factors[tmp] += 1
                tmp += i
        elif factors[i] == 4:
            count += 1
            if count == 4:
                return i - 3
        else:
            count = 0

print(problem047())

