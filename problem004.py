def isPalindrome(n):
    return str(n) == str(n)[::-1]

def problem004():
    a = [i*j for i in range(100, 1000) for j in range(i, 1000) if isPalindrome(i*j)]
    return max(a)

print(problem004())
