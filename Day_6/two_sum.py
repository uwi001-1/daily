#Return indices of the two numbers in an array such that they add up to a given target

def two_sum(nums, target):
    new = []
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                new.append(j)
                new.append(i)
    return new
nums = [1,5,8,2,5,9,6,4]
target = int(input("Enter the target:  "))
print(two_sum(nums, target))