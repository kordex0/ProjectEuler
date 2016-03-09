
coins = [200, 100, 50, 20, 10, 5, 2, 1]

def ways(n, maxcoin=0):
    if n < 1:
        return 0
    ans = 0
    
    i = maxcoin
    while coins[i] > n:
        i += 1
    if coins[i] == n:
        ans += 1
    while i < len(coins):
        ans += ways(n-coins[i], i)
        i += 1
    return ans
    

def problem031():
    return ways(200)

print(problem031())
