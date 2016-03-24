
include("primes.jl")
include("divisors.jl")

function problem021(n::Int)
    ans = 0
    primesl = primes(floor(Int, sqrt(n)))
    for a in 2:(n-1)
        b = properDivisorSum(a, primesl)
        if b > a
            if a == properDivisorSum(b, primesl)
                ans += a+b
            end
        end
    end
    return ans
end

println(problem021(10000))

