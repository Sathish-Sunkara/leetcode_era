from itertools import permutations
s="sathish"
li1=list(permutations(list(s),2))
li2=list(permutations(s,2))
print(li1==li2)

