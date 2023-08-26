"""matrix=[[1,1,1],[1,0,1],[1,1,1]]
a=len(matrix)
b=len(matrix[0])
l=[]
for i in range(a):
    for j in range(b):
        if matrix[i][j]==0:
            l.append((i,j))
for axis in l:
    for i in range(1,a):
        matrix[i][axis[1]]=0
for axis in l:
    for j in range(1,b):
        matrix[axis[0]][j]=0
print( matrix)"""

l=[[1, 2, 3], [2, 4, 1], [2, 1, 4]]
print(sorted(l))




