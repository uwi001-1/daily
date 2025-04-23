# Find if there exists a sublist in the given list with sum equals to target.

import itertools

def sublist_sum_equals(nums, target):
    for r in range(1, len(nums) + 1):  
        for subset in itertools.combinations(nums, r):
            if sum(subset) == target:
                return True
    return False

nums = list(map(int, input("Enter a list of numbers (space-separated): ").split()))
target = int(input("Enter the sum_target:  "))
print(sublist_sum_equals(nums, target))