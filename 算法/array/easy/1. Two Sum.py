"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# method_1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

"""
1. 用字典模拟哈希求解
2. 字典的索引效率远高于列表
"""

# method_2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index,value in enumerate(nums):
            sub = target - value
            if sub in hashmap:
                return [hashmap[sub],index]
            else:
                hashmap[value] = index

#method_3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for x in range(len(nums)):
            y = target - nums[x]
            if nums[x] in hashmap:
                return [hashmap[nums[x]], x]
            else:
                hashmap[y] = x


                
