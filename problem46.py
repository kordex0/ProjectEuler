primes = [2,3,5,7,11,13]

def nextprime(n):
    for i in primes:
        if i > n:
            return i
    return 0
            
def isprime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    
def cansumprime(n):
    i = 2
    while i != 0:
        for j in range(1, n):
            num = i + 2*j*j
            if num < n:
                continue
            elif num == n:
                print(n,'=',i,'+ 2 *',j,'^ 2')
                return True
            else:
                break
        i = nextprime(i)
    return False
    
for i in range(3, 9999, 2):
    if isprime(i):
        primes.append(i)
    else:
        if not cansumprime(i):
            print(i)
            break
