'''
Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]

Notes:

Each input will have exactly one solution.
You may not use the same element twice.
[execution time limit] 4 seconds (py3)

[input] array.integer numbers

[input] integer target

[output] array.integer
'''

def csSortedTwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
        