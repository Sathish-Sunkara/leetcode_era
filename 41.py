#first missing positive
nums = list(map(int,input("enter the list elements").split()))

print("list : " ,nums)

nums.append(0)

n = len(nums)

print(n)
flag = 1
for i in range(n):
    if nums[i]<0 or nums[i]>=n:
        nums[i] = 0
for i in range(n):
    nums[nums[i]%n] +=n
for i in range(1,n):
    if nums[i]/n == 0:
        print("positive is : ",i)
        flag = 0
        break
if flag:
    print("positive is : ",n)
