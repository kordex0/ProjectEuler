
include("primes.jl")

function problem110(n::Int)
    primesl = nprimes(max(ceil(Int, log(3, n)), 1))
    exponents = zeros(Int, length(primesl))
    
    ans = BigInt(1)
    for p in primesl
        ans *= p
    end
    
    n2 = 2*n
    counter = 1
    
    while true
        exponents[1] = 0
        divisors = 1
        for i in exponents
            divisors *= (2*i + 1)
        end
        exponents[1] = div(div(n2, divisors),2)
        
        while divisors*(2*exponents[1]+1) <= n2
            exponents[1] += 1 
        end
    
        if exponents[1] < exponents[2]
            counter += 1
        else
            num = BigInt(1)
            for i in 1:length(exponents)
                if exponents[i] == 0
                    break
                end
                num *= (BigInt(primesl[i])^exponents[i])
            end
            if num < ans
                ans = num
            end
            counter = 2
        end
        
        if counter > length(exponents)
            break
        end
        
        exponents[counter] += 1
        for i in 2:counter
            exponents[i] = exponents[counter]
        end
    end
    
    return ans
end

println(problem110(4*10^6))

