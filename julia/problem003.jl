
include("factors.jl")

function problem003(n::Int)
    return maximum(primeFactorSet(n))
end

println(problem003(600851475143))

