
function isPrime(n::Int)
    if n < 2
        return false
    elseif n == 2 or n == 3
        return true
    elseif n % 2 == 0 or n % 3 == 0
        return false
    end
    
    for i in 5:6:floor(Int, sqrt(n))
        if n % i == 0
            return false
        elseif n % (i+2) == 0
            return false
        end
    end
    
    return true
end

