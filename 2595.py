n=int(input("enter the values"))

b=bin(n)[2:]
b=str(b)
b=b[::-1]
even,odd=0,0
for i in range(len(b)):
    if i%2==0 and b[i]=='1':
        even+=1
    elif i%2!=0 and b[i]=='1':
        odd+=1
l=[even,odd]
print(l)
