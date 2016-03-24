
def fibGenerator():
    a = 0
    b = 1
    while True:
        tmp = a
        a = b
        b = tmp + b
        yield a

def problem025():
    for i, n in enumerate(fibGenerator()):
        if len(str(n)) >= 1000:
            return i+1

print(problem025())

