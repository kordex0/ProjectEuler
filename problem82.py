
matrix = []
weight = []

f = open("p081_matrix.txt")

for l in f:
    i = 0
    for n in l.split(','):
        if len(matrix) < i + 1:
            matrix.append([])
        matrix[j].append(int(n))
        i++

for i in range(0, len(matrix)):

    check = set()
    check.add((0,i))
    weight = []
    for a in range(0, len(matrix)):
        weight.append([])
        for b in range(0, len(matrix)):
            weight[a].append(0)
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
        if y > 0:
            newweight = myweight + matrix[x][y-1]
            if weight[x][y-1] == 0:
                weight[x][y-1] = newweight
                check.add((x,y-1))
            elif weight[x][y-1] > newweight:
                weight[x][y-1] = newweight
                check.add((x,y-1))
    print(min(weight[len(weight)-1]))
