
include("factors.jl")

function problem443(n::Int)
    i = 20
    while true
        k = div(minimum(primeFactorSet(2*i-1))-3, 2)
        if i + k + 1 > n
            break
        end
        i += k+1
    end
    return 3*i + (n - i)
end

println(problem443(10^15))

