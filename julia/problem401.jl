
include("divisors.jl")

function problem401(n::T)
    return divisorsSquaredSumSum(n)
end

println(problem401(BigInt(10^15)) % 10^9)
