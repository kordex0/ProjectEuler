
def problem001(n):
    # using PIE 
    ans = 0
    tmp = (n-1)//3
    ans += 3*((tmp*(tmp+1))/2)
    
    tmp = (n-1)//5
    ans += 5*((tmp*(tmp+1))/2)
    
    tmp = (n-1)//15
    ans -= 15*((tmp*(tmp+1))/2)
    return ans


print(problem001(1000))

