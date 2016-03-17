
def problem013(s):
    f = open(s)
    partial_total = 0
    for line in f:
        partial_total += int(line[:11])
    return int(str(partial_total)[:10])
    
print(problem013("problem013_input.txt"))

    
