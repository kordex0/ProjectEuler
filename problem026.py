
def repeatingDigits(n):
    numbers = []
    count = 0
    cur = 1
    
    while True:
        cur *= 10
        count += 1
        if cur in numbers:
            return count - numbers.index(cur) - 1
        numbers.append(cur)
        while(cur >= n):
            cur -= n
        if cur == 0:
            return 0

def problem026():
    results = map(repeatingDigits, range(1, 1000))
    return results.index(max(results)) + 1

print(problem026())
