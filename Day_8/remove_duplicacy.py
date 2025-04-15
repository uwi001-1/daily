# Array and Strings [Easy]
# Remove Duplicates from Sorted Array

# 1
def remove_duplicates(nums):
    new_list =set(nums)
    return list(new_list)

nums = [1,1,1,2,3,4,4,5]
print(remove_duplicates(nums))

# 2
def remove_duplicates(nums):
    count = 0
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)
            count += 1
    return new_list, count

nums = [1, 1, 1, 2, 3, 4, 4, 5]
new_list, count = remove_duplicates(nums)
print(new_list)   # Output: [1, 2, 3, 4, 5]
print(f'number of unique data : {count}')