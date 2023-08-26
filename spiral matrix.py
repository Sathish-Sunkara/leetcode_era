

mat = [[1,2,3],[4,5,6],[7,8,9]]

rowstart = 0
rowend = len(mat)-1
colstart = 0
colend = len(mat[0])-1
li = []

while rowstart <= rowend and colstart <= colend :

    #travesrse through the first row
    for i in range(colstart,colend+1):
        li.append(mat[rowstart][i])
    rowstart += 1
    for i in range(rowstart , rowend +1):
        li.append(mat[i][colend])
    colend -= 1
    if rowstart <= rowend:
        #then traverse last row right to left
        for i in range(colend , colstart-1 , -1):
            li.append(mat[rowend][i])
        rowend -= 1
    if colstart <= colend :
        for i in range(rowend,rowstart-1 ,-1):
            li.append(mat[i][colstart])
        colstart += 1
print(li)
    
        
        
