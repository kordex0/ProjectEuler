
using Benchmarks

function isPrime{T<:Integer}(n::T)
    if n < 2
        return false
    elseif n == 2 || n == 3
        return true
    elseif n % 2 == 0 || n % 3 == 0
        return false
    end
    
    for i in 5:6:floor(Int, sqrt(n))
        if n % i == 0
            return false
        elseif n % (i+2) == 0
            return false
        end
    end
    
    return true
end

function primes{T<:Integer}(n::T)
    if n < 2
        return T[]
    end
    primes = trues(Int(n))
    primes[1] = false
    for i in 4:2:n
        primes[i] = false
    end
    for i in 9:3:n
        primes[i] = false
    end
    for j in 5:6:floor(T, sqrt(n))
        for i in (j*j):j:n
            primes[i] = false
        end
        for i in ((j+2)*(j+2)):(j+2):n
            primes[i] = false
        end
    end
    primesn = T[]
    for i in 2:n
        if primes[i]
            push!(primesn, i)
        end
    end
    return primesn
end

function nprimes(n::Int)
    if n < 1
        return Int[]
    elseif n <= 16
        if n == 1
            return Int[2]
        else
            primesl = Int[2]
            i = 3
            while length(primesl) < n
                if isPrime(i)
                    push!(primesl, i)
                end
                i += 2
            end
            return primesl
        end
    else
        x = (2^floor(Int, log2(n)))*2
        if (x > 5395)
            epsilon = -1
        else
            epsilon = 2
        end
        
        while div(x, log(x)+epsilon) < n
            x *= 2
        end
        
        lower = div(x,2)
        upper = x
        mid = div(upper-lower,2) + lower
        if div(mid, log(mid)+epsilon) < n
            lower = mid
        else
            upper = mid
        end
        mid = div(upper-lower,2) + lower
        if div(mid, log(mid)+epsilon) < n
            return primes(upper)[1:n]
        else
            return primes(mid)[1:n]
        end
    end
end


