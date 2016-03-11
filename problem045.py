
def problem045():
    tn = 286
    T = 0
    pn = 166
    P = 0
    hn = 143
    H = 0
    while True:
        T = (tn*(tn + 1)) // 2
        while P < T:
            P = (pn*(3*pn - 1)) // 2 
            pn += 1
        while H < T:
            H = hn*(2*hn - 1)
            hn += 1
        if T == P and T == H:
            return T
        tn += 1

print(problem045())
