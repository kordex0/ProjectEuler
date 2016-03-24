
include("primes.jl")
include("divisors.jl")

function problem012(n::Int)
    primesl = primes(2^16)
    s = 3
    Ds = 2
    divisors = 2
    while divisors <= n
        s += 1
        ts = s
        if ts % 2 == 0
            ts = div(ts, 2)
        end
        Dts = divisorCount(ts, primesl)
        divisors = Ds*Dts
        Ds = Dts
    end
    return div(s*(s-1),2)
end

println(problem012(500))

