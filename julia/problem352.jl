
function problem352(n, p)
    a = ones(Float64, n)
    len = n
    pos = 1
    ans = n - 1
    
    a = [10,10,5]
    len = 3
    
    while true
        tmp = 0
        for i in 1:len
            if len == 5
                println(i, " ", a[i])
            end
            x = a[i]
            tmp += 1
            if x > 1
                tmpa = 1
                for j in 1:(x-1)
                    tmpa = 1 + p*(x-j) + (1-p)*tmpa
                end
                println("tmp ", tmpa)
                tmp += tmpa*(1-(1-p)^x)
                #tmp += (1-(1-p)^x)*x
            end
            if len == 5
                println(tmp)
            end
        end
        println(1 + tmp*(1-(1-p)^n))
        ans = min(tmp, ans)
        len -= 1
        if len == 1
            break
        end
        pos = max(1, mod(pos, len+1))
        for i in 1:a[len+1]
            a[pos] += 1
            pos = max(1, mod(pos+1, len+1))
        end
        #println(a)
        break
    end
    return ans
end

println(problem352(25, 0.02))

