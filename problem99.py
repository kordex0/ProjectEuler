
import math

f = open("p099_base_exp.txt")

nums = []
maps = {}

i = 1
for l in f:
    expnums = l.split(',')
    num = float(expnums[1]) * math.log(float(expnums[0]))
    maps[num] = i
    nums.append(num)
    
print(maps[max(nums)])
