
function isPrime(n::Int)
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

function primes(n::Int)
    if n < 2
        return Int[]
    end
    primes = trues(n)
    primes[1] = false
    for i in 4:2:n
        primes[i] = false
    end
    for i in 9:3:n
        primes[i] = false
    end
    for j in 5:6:floor(Int, sqrt(n))
        for i in (j*j):j:n
            primes[i] = false
        end
        for i in ((j+2)*(j+2)):(j+2):n
            primes[i] = false
        end
    end
    primesn = Int[]
    for i in 2:n
        if primes[i]
            push!(primesn, i)
        end
    end
    return primesn
end

