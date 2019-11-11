"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# method_1    利用python特性，list转换为set（136ms, 99.88%）
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# method_2    先排序，后逐一比较相邻元素（152ms）
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

# method_3    利用字典查重（144ms-232ms）
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if dic.get(i):
                return True
            dic[i] = 1
        return False
