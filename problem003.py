def problem003():
    n = 600851475143
    i = 3
    while True:
        while n % i == 0:
            if i == n:
                return i
            n /= i
        i += 2
    
print(problem003())
        
