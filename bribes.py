q = [1,2,5,3,4]
n = len(q)
flag = 0
arr = range(1,max(q)+1)
bribes = 0
for i in range(n):
    element = q[i]
    actual_index = element - 1
    index = q.index(element)
    if abs(actual_index - index) >= 3:
        print("choatic")
        flag = 1
        break
    bribes += actual_index - index
if not flag :
    print(bribes)
