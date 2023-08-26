nums = [5,1,2,3,4,6,7]
n= len(nums)
nums.sort()
num = nums[:n//2-1] + nums[n//2-1:][::-1]
print(num)
