
def problem002(n):
    # only even fibonacci numbers
    ans = 2
    e1 = 2
    e2 = 2
    next = 3*2 + 2
    while next < n:
        ans += next
        e1 = e2
        e2 = next
        next = next + e1 + 3*e2
    return ans

print(problem002(4 * 10**6))

