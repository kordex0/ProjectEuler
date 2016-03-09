
def problem029():
    s = set()
    for a in range(2, 101):
        for b in range(2,101):
            s.add(a**b)
    return len(s)

print(problem029())
