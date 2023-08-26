li=[1,2,3,4,5]
l=[]
while((len(li) > 1) or (len(li)!=0)):
    l.append(li.pop(0))
    l.append(li.pop())
            
if (len(li)==1):
    l.append(li.pop())

print(l)
