
import math

def problem024():
    nums = [0,1,2,3,4,5,6,7,8,9]
    ans = []
    pos = 1000000
    while pos > 0 and len(nums) > 0:
        i = 0
        while pos > math.factorial(len(nums)-1):
            pos -= math.factorial(len(nums)-1)
            i += 1
        ans.append(nums[i])
        del nums[i]
    ans += nums
    s = ""
    for c in ans:
        s += str(c)
    return int(s)

print(problem024())
