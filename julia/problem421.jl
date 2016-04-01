
using Benchmarks

include("primes.jl")

#n^17+1=(n+1)(n^2-n+1)(n^4-n^3+n^2-n+1)(n^8+n^7-n^5-n^4-n^3+n+1)
# all primes divide each part of the polynomial in a cycle
# ie 13 divides n(n-1)+1 when n = 4+13i or n = 10+13i

function a1(p) # n+1
    return Set{Int}([p-1])
end

function a2(p) # n(n-1)+1
    s = Set{Int}()
    num = 0
    for i in 1:p
        if (i*(BigInt(i)-1)+1) % p == 0
            push!(s, i)
            num += 1
        end
        if num == 2
            break
        end
    end
    return s
end

function a3(p) # n(n(n(n-1)+1)-1)+1
    s = Set{Int}()
    num = 0
    for i in 1:p
        if (i*(i*(i*(BigInt(i)-1)+1)-1)+1) % p == 0
            push!(s, i)
            num += 1
        end
        if num == 4
            break
        end
    end
    return s
end

function a4(p) # n(n(n(n(n(n(n(n+1))-1)-1)-1))+1)+1
    s = Set{Int}()
    num = 0
    for i in 1:p
        if (i*(i*(i*(i*(i*(i*(i*(BigInt(i)+1))-1)-1)-1))+1)+1) % p == 0
            push!(s, i)
            num += 1
        end
        if num == 8
            break
        end
    end
    return s
end

function S(n, m)
    primesl = primes(m)
    ans = BigInt(0)
    s = Set{Int}()
    for p in primesl
        if p == 2
            s = Set{Int}([3])
        else
            s = a1(p)
            s = union(s, a2(p))
            s = union(s, a3(p))
            s = union(s, a4(p))
        end
        for f in s
            ans += p * div(n + (p-f), p)
        end
    end
    return ans
end

println(S(BigInt(10)^11,10^4))

