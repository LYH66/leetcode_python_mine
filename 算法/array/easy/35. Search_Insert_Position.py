"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
#method_1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        for index in range(n):
            if nums[index] >= target:
                return index
        return n

#method_2   二分查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low
            
#method_3   内置函数list.index()
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if target in nums:
            return nums.index(target)
        for index in range(n):
            if nums[index] > target:
                return index
        return n

#method_4   index(), sorted()
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)

#method_5   神解法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([arg for arg in nums if arg < target])
#method_6
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else sorted([*nums, target]).index(target)
