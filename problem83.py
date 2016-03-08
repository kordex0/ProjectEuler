
matrix = []
weight = []

f = open("p081_matrix.txt")

i = 0
for l in f:
    matrix.append([])
    weight.append([])
    for n in l.split(','):
        matrix[i].append(int(n))
        weight[i].append(0)
    i += 1

check = set()
check.add((0,0))
weight[0][0] = matrix[0][0]

while len(check) > 0:
    (x,y) = check.pop()
    myweight = weight[x][y]
    if x < len(matrix) - 1:
        newweight = myweight + matrix[x+1][y]
        if weight[x+1][y] == 0:
            weight[x+1][y] = newweight
            check.add((x+1,y))
        elif weight[x+1][y] > newweight:
            weight[x+1][y] = newweight
            check.add((x+1,y))
    if y < len(matrix) - 1:
        newweight = myweight + matrix[x][y+1]
        if weight[x][y+1] == 0:
            weight[x][y+1] = newweight
            check.add((x,y+1))
        elif weight[x][y+1] > newweight:
            weight[x][y+1] = newweight
            check.add((x,y+1))
            
print(weight[len(matrix) - 1][len(matrix) - 1])
