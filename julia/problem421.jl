
using Benchmarks

import Base.div

include("primes.jl")

#Berlekamp's algorithm

#n^17+1=(n+1)(n^2-n+1)(n^4-n^3+n^2-n+1)(n^8+n^7-n^5-n^4-n^3+n+1)
# all primes divide each part of the polynomial in a cycle
# ie 13 divides n(n-1)+1 when n = 4+13i or n = 10+13i

function rem(a::Array, b::Array) # assume a[1] != 0 and b[1] = 1
    tmp = copy(a)
    denom = map(x -> 0-x, b[2:end])
    for i in 1:(length(a)-length(denom))
        for j in 1:length(denom)
            tmp[i+j] += tmp[i]*denom[j]
        end
    end
    return tmp[(length(tmp)-length(denom)+1):end]
end

function a1(p) # n+1
    return Set{Int}([p-1])
end

function a2(p) # n(n-1)+1 = n^2-n+1
    s = Set{Int}()
    num = 0
    for i in 1:p
        if ((i*((p+1)-i)) % p) == 1
            push!(s, i)
            push!(s, (p+1)-i)
            break
        end
    end
    return s
end

function a22(p) # n(n-1)+1 = n^2-n+1
    # BLEH
    # BI always = zeros for primes that work (for some reason)
    s = Set{Int}()
    deg = 2
    poly = [1,-1,1]
    B = zeros(Int, (deg,deg))
    B[1,1] = 1
    for i in 1:(deg-1)
        a = zeros(Int, (p*i))
        unshift!(a, 1)
        if length(a) >= length(poly)
            a = rem(a, poly)
        end
        if length(a) != deg
            prepend!(a, zeros(Int, deg-length(a)))
        end
        a = map(x -> mod(x, p), a)
        B[i+1,1:end] = reverse(a)
    end
    BI = map(x -> mod(x, p),B - eye(B))
    rank = 1 # compute this later
    k = deg - rank
    #kernel = Int[[1,1]]
    println(B)
    println(BI)
    #println(kernel)
    return s
end

println(a22(7))

function a3(p) # n(n(n(n-1)+1)-1)+1 = n^4-n^3+n^2-n+1
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

function a4(p) # n(n(n(n(n(n(n(n+1))-1)-1)-1))+1)+1 = n^8+n^7-n^5-n^4-n^3+n+1
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
            #s = union(s, a3(p))
            #s = union(s, a4(p))
        end
        for a in s
            ans += p * div(n + (p-a), p)
        end
    end
    return ans
end

function S2(n, m)
    primesl = primes(m)
    ans = BigInt(0)
    s = Set{Int}()
    for p in primesl
        if p == 2
            s = Set{Int}([3])
        else
            s = a1(p)
            s = union(s, a22(p))
            #s = union(s, a3(p))
            #s = union(s, a4(p))
        end
        for a in s
            ans += p * div(n + (p-a), p)
        end
    end
    return ans
end

#println(S(BigInt(10)^11,10^4))
#println(S2(BigInt(10)^11,10^4))

#println(@benchmark S(BigInt(10)^11,10^3))
#println(@benchmark S2(BigInt(10)^11,10^3))

