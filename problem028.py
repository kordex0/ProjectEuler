
def problem028():
    ans = 1
    for i in range(2, 502):
        j = (2*i) - 1
        tmp = j**2
        ans += tmp
        ans += (tmp-(j-2))
        ans += (tmp-2*(j-2))
        ans += (tmp-3*(j-2))
    return ans

print(problem028())
