
def isPalindrome(s):
    for i in range(len(s)/2):
        if not s[i] == s[-i-1]:
            return False
    return True

def problem036():
    ans = 0
    for i in range(1000000):
        if isPalindrome(str(i)) and isPalindrome("{0:b}".format(i)):
            ans += i
    return ans

print(problem036())
