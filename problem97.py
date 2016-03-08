

num = 28433

for i in range(0, 17957):
    num *= 2
    num = str(num)
    if len(num) > 10:
        num = num[-10:]
    num = int(num)

num += 1

print(num)
