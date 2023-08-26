def fun(s):
    flag=0
    for c in s:
        if c == "b" :
            flag=1
        if c == "a" and flag==1:
            return False
    return True


print(fun("aaaaa"))
