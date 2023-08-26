from collections import defaultdict
c = 0
l = ['rats','arts' , 'tars','star','tarr','atrr','war','raw','sam']
def isnibor(a,b):
    count = 0
    for k,v in zip(a,b):
        if len(a) != len(b):
            return False
        if k!=v:
            count+=1
    return count == 0 or count == 2
            



def dfs(node):
    seen.add(node)
    for val in graph[node]:
        if val not in seen:
            dfs(val)

graph = defaultdict(list)
print(graph)
n = len(l)
for i in range(n):
    for j in range(i+1,n):
        if isnibor(l[i],l[j]):
            graph[l[i]].append(l[j])
            graph[l[j]].append(l[i])
print(graph)

seen = set()
for i in range(n):
    if l[i] not in seen:
        dfs(l[i])
        c += 1
print(c)
        
