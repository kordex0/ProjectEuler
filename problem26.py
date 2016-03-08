
def num_repeating(bottom):
    numbers = []
    current = bottom

    count = 0
    
    num = 1

    while(True):
        num *= 10
        #print num
        count += 1
        try:
            place = numbers.index(num)
            return count - place - 1
        except Exception:
            pass
        numbers.append(num)
        while(num >= bottom):
            num -= bottom
            #print num
        if num == 0:
            return 0

results = map(num_repeating, xrange(1, 1000))
print results.index(max(results)) + 1

