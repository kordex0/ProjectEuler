
from helperfunctions import primes

def problem012(s):
    primesl = primes(65500)
    n = 3
    Dn = 2
    factors = 2
    # find D(n)D((n+1)/2) or D(n/2)D(n+1)
    while factors <= s:
        n += 1
        tn = n
        if tn % 2 == 0:
            tn //= 2
        Dtn = 1
        for p in primesl:
            if p*p > tn:
                Dtn *= 2
                break
            exponent = 1
            while tn % p == 0:
                exponent += 1;
                tn = tn//p;
            Dtn *= exponent
            if tn == 1:
                break
        factors = Dn*Dtn
        Dn = Dtn
    return (n*(n-1))//2
    
print(problem012(500))

