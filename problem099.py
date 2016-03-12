
import math

def problem099():
    f = open("problem099_base_exp.txt")
    
    nums = set()
    maps = {}
    
    for i, line in enumerate(f):
        expnums = line.split(',')
        num = float(expnums[1]) * math.log(float(expnums[0]))
        maps[num] = i+1
        nums.add(num)
    
    return maps[max(nums)]

print(problem099())

