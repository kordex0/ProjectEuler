
include("primes.jl")

function problem010(n::Int)
    return sum(primes(n))
end

println(problem010(2*10^6))

