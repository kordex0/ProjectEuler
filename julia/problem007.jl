
include("primes.jl")

function problem007(n::Int)
    return nprimes(n)[n]
end

println(problem007(10001))

