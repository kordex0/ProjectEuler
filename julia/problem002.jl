
function problem002(n::Int)
    ans = e1 = e2 = 2
    next = 4*2
    while next < n
        ans += next
        e1 = e2
        e2 = next
        next += e1 + 3*e2
    end
    return ans
end

println(problem002(4 * 10^6))

