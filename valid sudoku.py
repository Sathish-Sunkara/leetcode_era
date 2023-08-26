#valid sudoku
def valid(grid):
    rows = [[] for i in range(9)]
    
    cols = [[] for i in range(9)]

    box = [[] for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = grid[i][j]
            box_index = (i//3)*3 + (j//3)
            if num != "." :
                if num in rows or num in cols or num in box :
                    return False
                rows[i].append(num)
                cols[j].append(num)
                box[box_index].append(num)
    return True
                

grid =

result = valid(grid)

print("it is valid or not ? : ",result)

