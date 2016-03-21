
function problem001(n)
    fl3 = div(n-1, 3)
    fl5 = div(n-1, 5)
    fl15 = div(n-1, 15)
    return div(3*(fl3*(fl3+1)),2) + div(5*(fl5*(fl5+1)),2) - div(15*(fl15*(fl15+1)),2)
end

println(problem001(1000))

