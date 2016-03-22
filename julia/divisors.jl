
function divisorsCount(n::Int, primes::Array{Int})
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

