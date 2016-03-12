
def problem097():
    ans = 28433
    ans = ans * pow(2,7830457,10**10)
    ans += 1
    ans %= (10**10)
    
    return ans

print(problem097())
