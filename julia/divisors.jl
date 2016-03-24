
function divisorCount(n::Int, primes::Array{Int})
    divisors = 1
    for p in primes
        if p*p > n
            divisors *= 2
            break
        end
        if n % p == 0
            exponent = 2
            n = div(n, p)
            while n % p == 0
                exponent += 1
                n = div(n, p)
            end
            divisors *= exponent
        end
        if n == 1
            break
        end
    end
    return divisors
end

@inline function divisorCountPartial(n, i, divisors)
    if n % i == 0
        exponent = 2
        n = div(n, i)
        while n % i == 0
            exponent += 1
            n = div(n, 2)
        end
        divisors *= exponent
    end
    return n, divisors
end

function divisorCount(n::Int)
    if n == 1
        return 1
    elseif n < 1
        return 0
    end
    divisors = 1
    n, divisors = divisorCountPartial(n, 2, divisors)
    n, divisors = divisorCountPartial(n, 3, divisors)
    i = 5
    while i*i <= n
        n, divisors = divisorCountPartial(n, i, divisors)
        n, divisors = divisorCountPartial(n, i+2, divisors)
        i += 6
    end
    if n > 1
        divisors *= 2
    end
    return divisors
end

function divisorSum(n::Int, primes::Array{Int})
    sum = 1
    for p in primes
        if p*p > n
            if n > 1
                sum *= (n+1)
            end
            break
        end
        if n % p == 0
            s = p*p
            n = div(n, p)
            while n % p == 0
                s *= p
                n = div(n, p)
            end
            sum *= div(s-1, p-1)
        end
        if n == 1
            break
        end
    end
    return sum
end

function divisorSumPartial(n, i, sum)
    if n % i == 0
        s = i*i
        n = div(n, i)
        while n % i == 0
            s *= i
            n = div(n, i)
        end
        sum *= div(s-1, i-1)
    end
    return n, sum
end

function divisorSum(n::Int)
    if n < 1
        return 0
    end
    sum = 1
    n, sum = divisorSumPartial(n, 2, sum)
    n, sum = divisorSumPartial(n, 3, sum)
    i = 5
    while i*i <= n
        n, sum = divisorSumPartial(n, i, sum)
        n, sum = divisorSumPartial(n, i+2, sum)
        i += 6
    end
    if n > 1
        sum *= (n+1)
    end
    return sum
end

function properDivisorSum(n::Int, primes::Array{Int})
    return divisorSum(n, primes) - n
end

function properDivisorSum(n::Int)
    return divisorSum(n) - n
end

