#creating all sub arrays


def subarr(l):
    n= len(l)
    temp = []
    li = []
    for i in range(n,-1,-1):
        for j in range(0,i):
            temp =[]
            for k in range(j,i):
                temp.append(l[k])
            li.append(temp)
    return li



l = list(map(int,input("enter the list elements").split()))

print("the list is :" ,l)

print("sub arrays are :" ,subarr(l))


