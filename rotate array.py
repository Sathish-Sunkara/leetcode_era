#rotating arrays

from collections import deque

nums = [1,2,3,4,5,6]

print("original list : ",nums)

#rotate right elements at left (left rotate)
n = len(nums)

l = deque(nums)

l.rotate(-(n-2))  # place 5,6 at first (left rotate by 4)

l = list(l)

print("after left rotate ",l)


#rotate left elements at right

l = deque(nums)

l.rotate(n-2)

l = list(l )
print("after right rotate " ,l)
