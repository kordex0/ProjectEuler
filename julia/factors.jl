
using Benchmarks

@inline function primeFactorSetPartial{T}(s::Set{T}, n::T, i::T)
    if(n % i == 0)
        push!(s, i)
        n = div(n, i)
        while n % i == 0
            n = div(n, i)
        end
    end
    return n
end

function primeFactorSet{T}(n::T)
    s = Set{T}()
    i = T(2)
    n = primeFactorSetPartial(s, n, i)
    i += 1
    n = primeFactorSetPartial(s, n, i)
    
    i += 2
    while i <= n
        if i*i > n
            push!(s, n)
            break
        end
        n = primeFactorSetPartial(s, n, i)
        n = primeFactorSetPartial(s, n, i+2)
        i += 6
    end
    return s
end

