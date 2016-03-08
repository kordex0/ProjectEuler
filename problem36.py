
def doublepalindrome(n):
    nums = []
    tmp = n
    while tmp > 0:
        nums.append(tmp % 10)
        tmp /= 10
    for i in range(0, len(nums)/2):
        if not nums[i] == nums[-i-1]:
            return False
    nums = []
    tmp = n
    while tmp > 0:
        nums.append(tmp % 2)
        tmp /= 2
    for i in range(0, len(nums)/2):
        if not nums[i] == nums[-i-1]:
            return False
    return True

sum = 0
for i in range(1, 1000000):
    if doublepalindrome(i):
        sum += i
print(sum)
