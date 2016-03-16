
def isPalindrome(n):
    n = str(n)
    return n == n[::-1]

def problem004(n):
    a = [i*j for i in range(10**(n-1), 10**n) for j in range(i, 10**n) if isPalindrome(i*j)]
    return max(a)

print(problem004(3))

