import math

def checknum(n):
    sum = 0
    tmp = n
    while(tmp > 0):
        sum += math.factorial(tmp % 10)
        tmp = tmp / 10
    return sum == n


print(checknum(145))

sum = 0
for i in range(10,2540160):
    if(checknum(i)):
        sum += i
        print(i)
print sum


