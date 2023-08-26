def fun(nums):
    if nums==sorted(nums):
        return True
    flag=0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1] and flag == 1:
            return False
        if nums[i]>nums[i+1]:
            flag=1
    if nums[0] >= nums[-1]:
        return True
    else:
        return False

print(fun([6,10,6]))
