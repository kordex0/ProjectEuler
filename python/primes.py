
import math
from helperfunctions import range

def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0:
            return False
        if n % (i+2) == 0:
            return False
            
    return True

def primes(limit):
    if limit < 2:
        return []
    limit1 = limit-1
    primes = [True]*limit
    primes[0] = primes[1] = False
    
    primes[4:limit:2] = [False]*((limit1//2)-1)
    primes[9:limit:3] = [False]*((limit1//3)-2)
    
    for i in range(5, int(limit**0.5)+1, 6):
        if primes[i]:
            primes[i*i:limit:i] = [False]*((limit1//i)-i+1)
        if primes[i+2]:
            primes[(i+2)*(i+2):limit:(i+2)] = [False]*((limit1//(i+2))-i-1)
    
    return [i for i in range(limit) if primes[i]]

def nprimes(n):
    if n < 1:
        return []
    if n <= 16:
        if n == 1:
            return [2]
        else:
            primesl = [2]
            i = 3
            while len(primesl) < n:
                if isPrime(i):
                    primesl.append(i)
                i += 2
            return primesl
    else:
        x = int(2**(math.log(n)//math.log(2)))*2
        if (x > 5395):
            epsilon = -1
        else:
            epsilon = 2
        while x / (math.log(x)+epsilon) < n:
            x *= 2
            
        lower = x//2
        upper = x
        mid = ((upper-lower)//2) + lower
        if abs(mid / (math.log(mid)+epsilon)) < n:
            lower = mid
        else:
            upper = mid
        mid = ((upper-lower)//2) + lower
        if abs(mid / (math.log(mid)+epsilon)) < n:
            return primes(upper)
        else:
            return primes(mid)

