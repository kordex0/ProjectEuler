
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
    while i <= n
        if i*i > n
            divisors *= 2
            break
        end
        n, divisors = divisorCountPartial(n, i, divisors)
        n, divisors = divisorCountPartial(n, i+2, divisors)
        i += 6
    end
    return divisors
end

