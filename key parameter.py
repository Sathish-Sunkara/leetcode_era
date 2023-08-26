def fun(x):
    return x**2
l=[-3,-2,-1,0,1,2,3,-4]
print(l)
l=sorted(l)
print(l)
l=sorted(l,key=fun)
print(l)
