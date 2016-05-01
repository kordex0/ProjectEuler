
using Benchmarks

include("primes.jl")

@inline function divisorCountPartial{T<:Integer}(n::T, i::T, divisors::T)
    if n % i == 0
        exponent = T(2)
        n = div(n, i)
        while n % i == 0
            exponent += 1
            n = div(n, i)
        end
        divisors *= exponent
    end
    return n, divisors
end

function divisorCount{T<:Integer}(n::T, primes::AbstractArray{T})
    if n == 1
        return 1
    elseif n < 1
        return 0
    end
    divisors = T(1)
    for p in primes
        if p*p > n
            if n > 1
                divisors *= 2
            end
            break
        end
        n, divisors = divisorCountPartial(n, p, divisors)
        if n == 1
            break
        end
    end
    return divisors
end

function divisorCount{T<:Integer}(n::T)
    divisors = T(1)
    n, divisors = divisorCountPartial(n, T(2), divisors)
    n, divisors = divisorCountPartial(n, T(3), divisors)
    i = T(5)
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

@inline function divisorSumPartial{T<:Integer}(n::T, i::T, sum::T)
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

function divisorSum{T<:Integer}(n::T, primes::AbstractArray{T})
    if n < 1
        return 0
    end
    sum = T(1)
    sqrtn = floor(T, sqrt(n))
    for p in primes
        if p > sqrtn
            if n > 1
                sum *= (n+1)
            end
            break
        end
        n, sum = divisorSumPartial(n, p, sum)
        if n == 1
            break
        end
    end
    return sum
end

function divisorSum{T<:Integer}(n::T)
    if n < 1
        return 0
    end
    sum = T(1)
    n, sum = divisorSumPartial(n, T(2), sum)
    n, sum = divisorSumPartial(n, T(3), sum)
    i = T(5)
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

function properDivisorSum{T<:Integer}(n::T, primes::AbstractArray{T})
    return divisorSum(n, primes) - n
end

function properDivisorSum{T<:Integer}(n::T)
    return divisorSum(n) - n
end

function divisorSumSum{T<:Integer}(n::T)
    sum = T(0)
    i = T(1)
    while i <= n
        ni = div(n, i)
        j = div(n, ni) + 1
        sum += div(ni * (i + j - 1) * (j - i), 2)
        # multiplier of number [i,j) to divide n is n/i
        # avg value of these numbers is (i+j-1)/2
        # number of numbers is j - i
        # ie for 12, 5 and 6 both divide twice
        # (4 divides 3 times and 7 divides once)
        # i = 5, j = 7
        # 5*2 + 6*2 =  12/5 * (5+7-1)/2 * (7-5) = 2 * 5.5 * 2
        i = j
    end
    return sum
end

function properDivisorSumSum{T<:Integer}(n::T)
    return divisorSumSum(n) - div(n*(n+1),2)
end

function divisorSquaredSumSum{T<:Integer}(n::T)
    sum = T(0)
    i = T(1)
    while i <= n
        ni = div(n, i)
        j = div(n, ni) + 1
        # sum of squared numbers from i to j-1
        sum += div(ni * ((j-1)*(j)*(2*j-1)-(i-1)*(i)*(2*i-1)), 6)
        i = j
    end
    return sum
end




