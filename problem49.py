
def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
    return True
    
    
nums = {}
for i in [1234,1324,2341]:
    s = sorted([int(a) for a in str(i)])
    key = (s[0],s[1],s[2],s[3])
    if not nums.get(key,None):
        nums[key] = []
    nums[key].append(i)
print(nums)
for key,val in nums.items():
    if len(val) >= 3:
        print(key)
        print(val)
