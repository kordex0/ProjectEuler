
def problem092():
    ans = 0
    ends1 = set([1])
    ends89 = set([89])
    partial = set()
    
    for i in range(1,10000000):
        if i > 600:
            i = sum([int(c)**2 for c in str(i)])
            if i in ends1:
                continue
            if i in ends89:
                ans += 1
                continue
        
        partial.clear()
        while True:
            if i in ends1:
                ends1 = ends1.union(partial)
                break
            if i in ends89:
                ends89 = ends89.union(partial)
                ans += 1
                break
            partial.add(i)
            i = sum(int(c)**2 for c in str(i))
    return ans

print(problem092())
