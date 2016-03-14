
def isPalindrome(n):
    n = str(n)
    return n == n[::-1]

def isProbablyLychrel(n):
    
    for i in range(51):
        n += int(str(n)[::-1])
        if isPalindrome(n):
            return False
    return True

def problem055():

    ans = 0
    for i in range(10000):
        if isProbablyLychrel(i):
            ans += 1
    
    return ans

print(problem055())
