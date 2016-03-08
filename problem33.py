
a = 1
b = 1

def cancels(a, b):
    al = a / 10
    ar = a % 10
    bl = b / 10
    br = b % 10

    if(al == br and ar != 0 and bl != 0 and ((a / float(ar)) == (b / float(bl)))):
        print a, b
    if(ar == bl and al != 0 and br != 0 and ((a / float(al)) == (b / float(br)))):
        print a, b


for a in range(1, 100) :
    for b in range(a + 1, 100):
        cancels(a, b)
