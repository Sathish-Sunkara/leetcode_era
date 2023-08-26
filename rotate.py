l = list(map(int,input().split()))
def to(l):
    n = len(l)
    flag = 0
    c = 0
    for i in range(n-1):
        if l[i] > l[i+1]:
            c+=1
            flag = 1
        if flag and l[i] > l[i+1]:
            
            return False
    if l[-1] < l[0]:
        return False
    return True


print(to(l))
