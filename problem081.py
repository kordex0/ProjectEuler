
def problem081():
    f = open("problem081_matrix.txt")
    
    mat = []
    for line in f:
        mat.append(map(int, line.split(",")))
        
    height = len(mat)
    width = len(mat[0])
        
    weight = []
    for i in range(height):
        weight.append([0]*width)
    
    weight[0][0] = mat[0][0]
    
    check = set()
    check.add((0,0))
    
    while len(check) > 0:
        x, y = check.pop()
        if x < (height-1):
            tmp = weight[x][y] + mat[x+1][y]
            if weight[x+1][y] == 0 or weight[x+1][y] > tmp:
                weight[x+1][y] = tmp
                check.add((x+1, y))
        if y < (width-1):
            tmp = weight[x][y] + mat[x][y+1]
            if weight[x][y+1] == 0 or weight[x][y+1] > tmp:
                weight[x][y+1] = tmp
                check.add((x, y+1))
    
    return weight[height-1][width-1]

print(problem081())
