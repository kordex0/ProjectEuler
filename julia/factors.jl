
@inline function primeFactorSetPartial(s::Set{Int}, n::Int, i::Int)
    if(n % i == 0)
        push!(s, i)
        n = div(n, i)
        while n % i == 0
            n = div(n, i)
        end
    end
    return n
end

function primeFactorSet(n::Int)
    s = Set{Int}()
    n = primeFactorSetPartial(s, n, 2)
    n = primeFactorSetPartial(s, n, 3)
    
    i = 5
    while i <= n
        if i*i > n
            push!(s, n)
            n = 1
            break
        end
        n = primeFactorSetPartial(s, n, i)
        n = primeFactorSetPartial(s, n, i+2)
        i += 6
    end
    return s
end

