import itertools

tmp = ""
for i in range(0, 10):
    tmp += str(i)

count = 0
for perm in itertools.permutations(tmp):
    s = "".join(perm)
    i = s[1:4]
    if not int(i) % 2 == 0:
        continue
    i = s[2:5]
    if not int(i) % 3 == 0:
        continue
    i = s[3:6]
    if not int(i) % 5 == 0:
        continue
    i = s[4:7]
    if not int(i) % 7 == 0:
        continue
    i = s[5:8]
    if not int(i) % 11 == 0:
        continue
    i = s[6:9]
    if not int(i) % 13 == 0:
        continue
    i = s[7:]
    if not int(i) % 17 == 0:
        continue
    count += int(s)

print(count)
