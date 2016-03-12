
def problem082():
    f = open("problem082_matrix.txt")
    
    mat = []
    for line in f:
        mat.append(map(int, line.split(",")))
        
    height = len(mat)
    width = len(mat[0])
    
    ans = sum(mat[0])
    
    for i in range(height):
        weight = []
        for j in range(height):
            weight.append([0]*width)
        
        weight[i][0] = mat[i][0]
        
        check = set()
        check.add((i,0))
        
        while len(check) > 0:
            x, y = check.pop()
            if x < (height-1):
                tmp = weight[x][y] + mat[x+1][y]
                if weight[x+1][y] == 0 or weight[x+1][y] > tmp:
                    weight[x+1][y] = tmp
                    check.add((x+1, y))
            if x > 0:
                tmp = weight[x][y] + mat[x-1][y]
                if weight[x-1][y] == 0 or weight[x-1][y] > tmp:
                    weight[x-1][y] = tmp
                    check.add((x-1, y))
            if y < (width-1):
                tmp = weight[x][y] + mat[x][y+1]
                if weight[x][y+1] == 0 or weight[x][y+1] > tmp:
                    weight[x][y+1] = tmp
                    if y < (width-2):
                        check.add((x, y+1))
        
        for j in range(height):
            ans = min(ans, weight[j][width-1])
            
    return ans

print(problem082())
