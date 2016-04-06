
using Benchmarks

include("primes.jl")
include("factors.jl")

function pow(a::Int, b::Int, c::Int) # faster than powermod
    ans = 1
    while b > 0
        if b % 2 == 1
            ans = mod(ans*a, c)
            b -= 1
        end
        b = div(b, 2)
        a = mod(a*a, c)
    end
    return ans
end

function primitiveroot(p::Int, primesl::Array{Int})
    phi = p - 1
    factors = primeFactorSet(phi, primesl)
    for i in 1:phi
        primitive = true
        for f in factors
            if pow(i, div(phi, f), p) == 1
                primitive = false
                break
            end
        end
        if primitive
            return i
        end
    end
end

# (-x)^15 = 1 (mod p) <=> (x)^15 = -1 (mod p)
function pthunity(p::Int, primesl::Array{Int})
    d = gcd(15, p-1)
    g = primitiveroot(p, primesl)
    h = pow(g, div(p-1,d), p)
    return sort([(p - pow(h, t, p)) for t in 0:(d-1)]) # (p-x)
end

function problem421(n, m)
    primesl = primes(m)
    ans = 0
    for p in primesl
        ar = pthunity(p, primesl)
        for a in ar
            if n >= a
                ans += p * (div(n-a, p) + 1)
            end
        end
    end
    return ans
end

println(problem421(10^11,10^3))

println(@benchmark problem421(10^11,10^6))

